import logging
 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
 
logger = logging.getLogger(__name__)

def bonus_calculator (basic_salary, designation):
    
    logger.info("Calculating bonus")
    
    designation=designation.lower()
    
    if designation == "coder":
        logger.info(f"Bonus Calculated")
        return 0.1 * basic_salary
    elif designation == "designer":
        logger.info(f"Bonus Calculated")
        return 0.15 * basic_salary
    elif designation == "manager":
        logger.info(f"Bonus Calculated")
        return 0.05 * basic_salary
    else:
        logger.warning("Unknown Designation received")
        return 0
    
    
          
    
