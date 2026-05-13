"""
PROBLEM DESCRIPTION:
As a GIS Analyst, identifying 'at-risk' zones based on proximity to a hazard is a core task. 
This program reads a list of 'Critical Infrastructure' locations from a text file. 
Each entry includes a name and (x, y) coordinates. The user inputs the coordinates 
of a detected wildfire and a 'danger radius.' The program calculates the Euclidean 
distance to each facility, determines which fall within the danger zone, 
and exports an 'Evacuation Report' for facilities needing immediate action.
"""

import math

# Requirement 2c: User-defined function for solving a meaningful subproblem
def calculate_distance(x1, y1, x2, y2):
    """Calculates the straight-line distance between two coordinate points."""
    # Requirement 2c: Arithmetic expressions
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def main():
    # Requirement 2c: Variable declarations and assignments
    infrastructure_data = []
    at_risk_facilities = []
    total_distance = 0
    count = 0

    # Requirement 2c: Read input from a file
    try:
        input_file = open("locations.txt", "r")
        # Requirement 2c: Sequence iteration using a for loop
        for line in input_file:
            # Cleaning and splitting the string data
            parts = line.strip().split(",")
            if len(parts) == 3:
                name = parts[0]
                # Requirement 2c: Sequence types (tuples/lists)
                coords = (float(parts[1]), float(parts[2]))
                infrastructure_data.append([name, coords])
        input_file.close()
    except FileNotFoundError:
        print("Error: locations.txt not found. Please create the file first.")
        return

    # Requirement 2c: Use of a while loop for general iteration
    keep_running = True
    while keep_running:
        print("\n--- GIS Wildfire Proximity Analysis Tool ---")
        
        # User input for the current fire scenario
        fire_x = float(input("Enter Fire X-Coordinate: "))
        fire_y = float(input("Enter Fire Y-Coordinate: "))
        radius = float(input("Enter Danger Radius (km): "))

        print(f"\nAnalyzing facilities within {radius}km of ({fire_x}, {fire_y})...")
        
        # Requirement 2c: Use of sequence types and iteration
        for item in infrastructure_data:
            name = item[0]
            facility_x = item[1][0]
            facility_y = item[1][1]
            
            # Use the defined function
            dist = calculate_distance(fire_x, fire_y, facility_x, facility_y)
            total_distance += dist
            count += 1
            
            # Requirement 2c: Use of if/elif/else statements
            if dist <= radius:
                status = "EVACUATE IMMEDIATELY"
                at_risk_facilities.append(f"{name} (Distance: {dist:.2f}km)")
            elif dist <= radius * 1.5:
                status = "HIGH ALERT"
            else:
                status = "SAFE"
            
            # Requirement 2c: Print statements for output
            print(f"- {name:25} | Distance: {dist:6.2f}km | Status: {status}")

        # Requirement 2c: Write output to a file
        output_file = open("evacuation_report.txt", "w")
        output_file.write("CRITICAL EVACUATE LIST\n")
        output_file.write("======================\n")
        for facility in at_risk_facilities:
            output_file.write(facility + "\n")
        output_file.close()
        
        print(f"\nReport generated. {len(at_risk_facilities)} facilities are at risk.")
        
        # Control the while loop
        choice = input("\nRun another scenario? (yes/no): ").lower()
        if choice != "yes":
            keep_running = False

    print("Analysis complete. Stay safe.")

if __name__ == "__main__":
    main()