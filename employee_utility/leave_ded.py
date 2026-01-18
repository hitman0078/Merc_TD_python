import logging
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
logger = logging.getLogger(__name__)

def calculate_leave_deduction(basic_salary, leaves_taken):
    
    logger.info("Calculating Leave Deduction")

    total_working_days = 30
    paid_leaves = 15
 
    per_day_salary = basic_salary / total_working_days
 
    if leaves_taken > paid_leaves:
        extra_leaves = leaves_taken - paid_leaves
        logger.info("Deduction Calculated")
        return extra_leaves * per_day_salary
    else:
        return 0
    
    