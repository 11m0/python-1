import argparse
parser = argparse.ArgumentParser(description='Calculation of employee salaries')
parser.add_argument('prod', type=float, help='Input output in hours')
parser.add_argument('rate', type=float, help='Input rate per hour')
parser.add_argument('award', type=float, help='Input the award')
args = parser.parse_args()
print(f'The salary of employee is: {args.prod * args.rate + args.award}')
