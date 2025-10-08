import requests


import numpy as np
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)


# Hermes Pyth API documentation: https://hermes.pyth.network/docs/

TOKEN_MAP = {
    "BTC": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43",
    "ETH": "ff61491a931112ddf1bd8147cd1b641375f79f5825126d665480874634fd0ace",
    "XAU": "765d2ba906dbc32ca17cc11f5310a89e9ee1f6420508c63861f2f8ba4ee34bb2",
    "SOL": "ef0d8b6fda2ceba41da15d4095d1da392a0d2f8ed0c6c7bc0f4cfac8c280b56d",
}

pyth_base_url = "https://hermes.pyth.network/v2/updates/price/latest"


@retry(
    stop=stop_after_attempt(5),
    wait=wait_random_exponential(multiplier=2),
    reraise=True,
)
def get_asset_price(asset="BTC"):
    pyth_params = {"ids[]": [TOKEN_MAP[asset]]}
    response = requests.get(pyth_base_url, params=pyth_params)
    if response.status_code != 200:
        print("Error in response of Pyth API")
        return

    data = response.json()
    parsed_data = data.get("parsed", [])

    asset = parsed_data[0]
    price = int(asset["price"]["price"])
    expo = int(asset["price"]["expo"])

    live_price = price * (10**expo)

    return live_price


def simulate_single_price_path_gbm(current_price, time_increment, time_length, sigma, mu=0):
    one_hour = 3600
    dt = time_increment / one_hour
    num_steps = int(time_length / time_increment)

    # lognormal increments with drift correction
    increments = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.normal(size=num_steps)
    cumulative_returns = np.exp(np.cumsum(increments))
    cumulative_returns = np.insert(cumulative_returns, 0, 1.0)

    price_path = current_price * cumulative_returns
    return price_path

def simulate_price_path_logOU(
    current_price,
    time_increment,
    time_length,
    sigma,
    theta=0.1,
    mu=0,  # long-term mean of log-price drift
):
    """
    Simulate a log-Ornstein–Uhlenbeck (mean-reverting in log space) price path.

    Parameters:
        current_price : float
            Starting price (e.g., 100_000)
        time_increment : float
            Step size in seconds (e.g., 300 for 5 minutes)
        time_length : float
            Total simulation horizon in seconds (e.g., 24*3600)
        sigma : float
            Annualized volatility (e.g., 0.3)
        theta : float
            Mean reversion speed (higher = faster reversion)
        mu : float
            Long-term mean of the *log-price* (0 keeps it centered)

    Returns:
        np.ndarray : Simulated price path (length N+1)
    """

    one_hour = 3600
    dt = time_increment / one_hour  # time step in hours
    num_steps = int(time_length / time_increment)

    # Convert sigma from annualized to hourly
    hours_in_year = 365 * 24
    sigma_hourly = sigma / np.sqrt(hours_in_year)

    # Initialize arrays
    log_price = np.zeros(num_steps + 1)
    log_price[0] = np.log(current_price)

    for t in range(1, num_steps + 1):
        # Mean reversion term: pull back toward mu
        drift = theta * (mu - log_price[t - 1]) * dt
        diffusion = sigma_hourly * np.sqrt(dt) * np.random.normal()
        log_price[t] = log_price[t - 1] + drift + diffusion

    return np.exp(log_price)

def simulate_crypto_price_paths(
    current_price, time_increment, time_length, num_simulations, sigma, func_name
):
    """
    Simulate multiple crypto asset price paths.
    """

    price_paths = []
    for _ in range(num_simulations):
        price_path = globals()[func_name](
            current_price, time_increment, time_length, sigma
        )
        price_paths.append(price_path)

    return np.array(price_paths)
