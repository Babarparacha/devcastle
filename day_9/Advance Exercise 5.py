import statistics
from abc import ABC, abstractmethod
from dataclasses import dataclass


# ==========================================
# PHASE 1: TRANSFORM (Read & Clean the File)
# ==========================================
def load_and_clean_data(filename):
    print(f"--- 1. Reading and Cleaning Data from {filename} ---")
    clean_prices = []
    
    try:
        # Day 6: File Handling using 'with' (automatically closes the file)
        with open(filename, "r") as file:
            raw_lines = file.readlines()
            
            for line in raw_lines:
                stripped_line = line.strip()
                
                # Day 5: Control Flow (Skip blanks)
                if stripped_line == "":
                    continue
                
                # Day 6: Exception Handling (Catching "N/A" and converting to int)
                try:
                    price = int(stripped_line)
                    if price > 0:  # Only keep valid positive prices
                        clean_prices.append(price)
                except ValueError:
                    pass # Ignore text errors silently
                    
    except FileNotFoundError:
        print(f"CRITICAL ERROR: {filename} not found.")
        quit()
        return []

    print(f"Data Cleaned! Recovered {len(clean_prices)} valid property prices.\n")
    return clean_prices


# ==========================================
# PHASE 2: LOAD (Advanced OOP Architecture)
# ==========================================

# 1. Data Class (Holds the clean data securely)
@dataclass
class NeighborhoodData:
    name: str
    prices: list

# 2. Abstract Base Class (The Strict Contract)
class BaseAnalyzer(ABC):
    def __init__(self, data_object: NeighborhoodData):
        self.data_object = data_object

    @abstractmethod
    def generate_report(self):
        pass

# 3. Polymorphism Child 1 (Quick Stats)
class QuickMarketAnalyzer(BaseAnalyzer):
    def generate_report(self):
        prices = self.data_object.prices
        avg = statistics.mean(prices)
        mid = statistics.median(prices)
        
        print(f"---Quick Report: {self.data_object.name} ---")
        print(f"Mean: Rs. {avg:,.2f} | Median: Rs. {mid:,.2f}")
        if avg > (mid * 1.5):
            print("High Variance Detected. Trust the Median.")
        print("-" * 40)

# 4. Polymorphism Child 2 (Deep Stats & Mode)
class DeepMarketAnalyzer(BaseAnalyzer):
    def generate_report(self):
        prices = self.data_object.prices
        print(f"---Deep Analysis: {self.data_object.name} ---")
        print(f"Total Valid Listings: {len(prices)}")
        print(f"Mean: Rs. {statistics.mean(prices):,.2f}")
        print(f"Median: Rs. {statistics.median(prices):,.2f}")
        
        try:
            popular = statistics.mode(prices)
            print(f"Mode (Most Common): Rs. {popular:,.2f}")
        except statistics.StatisticsError:
            print("Mode: No single most common price.")
        print("-" * 40)


# ==========================================
# EXECUTION: RUNNING THE FULL PIPELINE
# ==========================================

# Step 1: Generate the messy file

# Step 2: Extract and Clean the data
valid_prices = load_and_clean_data("market_dump.txt")

# Step 3: Load the clean data into our Data Class
market_data = NeighborhoodData(name="Bahawalnagar Commercial Zone", prices=valid_prices)
print(type(market_data))
# Step 4: Run the polymorphic AI analyzers
print("--- 2. Running AI Analyzers ---")
analyzers = [QuickMarketAnalyzer(market_data),DeepMarketAnalyzer(market_data)]

for engine in analyzers:
    engine.generate_report()