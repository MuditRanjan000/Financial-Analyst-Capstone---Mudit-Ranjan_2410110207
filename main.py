from graph import app

def main():
    print("--- Financial News Analyst Agent ---")
    print("Enter a company ticker to generate an investment memo.")
    
    while True:
        company = input("\nEnter Ticker (e.g., TSLA, AAPL, MSFT) or 'q' to quit: ").strip().upper()
        
        if company.lower() == 'q':
            print("Exiting...")
            break
            
        if not company:
            continue
            
        print(f"\nStarting analysis for {company}...\n")
        
        # Initialize the state with the user's input
        # Note: We only need to provide the required input fields
        initial_state = {
            "company_name": company,
            "stock_data": "",
            "news_articles": [],
            "final_report": ""
        }
        
        # Invoke the graph
        result = app.invoke(initial_state)
        
        print("\n" + "="*50)
        print("FINAL REPORT")
        print("="*50)
        print(result["final_report"])
        print("="*50)

if __name__ == "__main__":
    main()