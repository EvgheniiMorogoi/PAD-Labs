import logging
import azure.functions as func

app = func.FunctionApp()

@app.timer_trigger(schedule="0/10 * * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def timer_triggerPADTestEMI(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')