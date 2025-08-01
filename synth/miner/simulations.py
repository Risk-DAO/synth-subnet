from synth.miner.price_simulation import (
    simulate_crypto_price_paths,
    get_asset_price,
)
from synth.utils.helpers import (
    convert_prices_to_time_format,
)

import requests
from datetime import datetime, timedelta, timezone
import math

def fetch_volatility(asset_name):
    url = "https://deribit-2eb46cdf4c7a.herokuapp.com/volatility"
    params = {"asset": asset_name}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # raises HTTPError for status codes >= 400
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON: {e}")
        return None

def is_timestamp_recent(timestamp_str, max_age_hours=2):
    """
    Check if the timestamp (ISO format) is within max_age_hours from now (UTC).
    """
    try:
        ts = datetime.fromisoformat(timestamp_str)
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        return now - ts <= timedelta(hours=max_age_hours)
    except Exception as e:
        print(f"Error parsing timestamp: {e}")
        return False

def generate_simulations(
    asset="BTC",
    start_time: str = "",
    time_increment=300,
    time_length=86400,
    num_simulations=1,
    sigma=0.01,
):
    """
    Generate simulated price paths.

    Parameters:
        asset (str): The asset to simulate. Default is 'BTC'.
        start_time (str): The start time of the simulation. Defaults to current time.
        time_increment (int): Time increment in seconds.
        time_length (int): Total time length in seconds.
        num_simulations (int): Number of simulation runs.
        sigma (float): Standard deviation of the simulated price path.

    Returns:
        numpy.ndarray: Simulated price paths.
    """
    if start_time == "":
        raise ValueError("Start time must be provided.")

    current_price = get_asset_price(asset)
    if current_price is None:
        raise ValueError(f"Failed to fetch current price for asset: {asset}")
    xxx_json = fetch_volatility(asset)
    default_sigma = sigma = 0.003
    sqrt24 = math.sqrt(24)
    sigma = float(xxx_json["simple_avg_vol"]) / sqrt24
    if not is_timestamp_recent(xxx_json["timestamp"]):
        sigma = default_sigma * 1    
    print(f"asset {asset}, sigma {sigma}, jsons {xxx_json}")
            
    simulations = simulate_crypto_price_paths(
        current_price=current_price,
        time_increment=time_increment,
        time_length=time_length,
        num_simulations=num_simulations,
        sigma=sigma,
    )

    predictions = convert_prices_to_time_format(
        simulations.tolist(), start_time, time_increment
    )

    return predictions
