import xml.etree.ElementTree as ET
import csv

# File paths
input_file = 'export.xml'  # Replace with your export.xml file path
output_file = 'export.csv'  # Replace with desired output CSV file name

# Parse the XML file
tree = ET.parse(input_file)
root = tree.getroot()

# Prepare CSV file
with open(output_file, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row based on XML structure
    headers = ['type', 'value', 'unit', 'startDate', 'endDate']
    writer.writerow(headers)

    # Iterate through records in XML and write to CSV
    for record in root.findall('Record'):
        record_type = record.get('type', '').strip()
        value = record.get('value', '').strip()
        unit = record.get('unit', '').strip()
        start_date = record.get('startDate', '').strip()
        end_date = record.get('endDate', '').strip()

        # Skip rows that have no meaningful data
        if any([record_type, value, unit, start_date, end_date]):
            writer.writerow([record_type, value, unit, start_date, end_date])

print(f'CSV file saved as {output_file}')
