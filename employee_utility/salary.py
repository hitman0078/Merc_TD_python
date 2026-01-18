import logging
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
logger = logging.getLogger(__name__)

from bonus import bonus_calculator
from leave_ded import calculate_leave_deduction

def calculate_final_salary(basic_salary, designation, leaves_taken):
    
    logger.info("Starting Final Salary Calculation")

    bonus = bonus_calculator(basic_salary, designation)
    deduction = calculate_leave_deduction(basic_salary, leaves_taken)
 
    final_salary = basic_salary + bonus - deduction
    logger.info(f"Final Salary Calculated:{final_salary}")
    return final_salary