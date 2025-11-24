import os
import yfinance as yf
from langchain_core.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv

# Load environment variables to get the TAVILY_API_KEY
load_dotenv()

# --- Tool 1: Stock Price Fetcher ---
@tool
def get_stock_prices(ticker: str):
    """
    Fetches the current stock price and basic info for a given ticker symbol.
    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'TSLA').
    """
    print(f"--- Fetching stock data for: {ticker} ---")
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        currency = stock.info.get('currency', 'USD')
        return f"Current price of {ticker}: {price:.2f} {currency}"
    except Exception as e:
        return f"Error fetching stock data for {ticker}: {e}"

# --- Tool 2: Market News Search ---
@tool
def search_market_news(query: str):
    """
    Searches for the latest financial news about a specific company or market topic.
    Args:
        query (str): The search query (e.g., 'Tesla stock news', 'Apple strategic moves').
    """
    print(f"--- Searching news for: {query} ---")
    try:
        # We typically want raw content to feed into the LLM for synthesis
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = tavily.search(query=query, max_results=3)
        
        # Format the results into a single string
        results = response.get("results", [])
        formatted_results = "\n".join([
            f"- {r['title']}: {r['content']} (Source: {r['url']})"
            for r in results
        ])
        return formatted_results
    except Exception as e:
        return f"Error searching news: {e}"