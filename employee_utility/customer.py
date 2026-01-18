import logging
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
logger = logging.getLogger(__name__)

from salary import calculate_final_salary
 
basic_salary = 190
designation = "coder"
leaves_taken = 3
 
final_salary = calculate_final_salary(
    basic_salary,
    designation,
    leaves_taken
)
 
print("Final Salary:", final_salary)
