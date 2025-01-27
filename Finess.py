import argparse
from ParseFile import ParseFile
from GetRankings import GetRankings
from Deshboards import Dashboards

def main():
    #get cli input
    parser = argparse.ArgumentParser(description="Parse fitness goals from a file.")
    parser.add_argument("week", help="week number")
    args = parser.parse_args()
    
    #get parsed results from list
    parsed_results = ParseFile(args.week + ".txt", args.week)
    
    #create groups and individual rankings
    rankings = GetRankings(parsed_results.get_result(), args.week)
    
    #accumulated_rankings
    print(rankings.get_accumulated_individual())
    
    Dashboards(rankings, args.week)
    
if __name__ == "__main__":
    main()