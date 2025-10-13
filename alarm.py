#Skapa larm
class Alarm:
    def __init__(self, alarm_type, threshold: int):
        self.alarm_type = alarm_type #cpu, ram, disk
        self.threshold  = threshold #warning %
        self.triggered = False #if alarm triggered

    def check_trigger(self, current_value: float) -> bool:
        '''Return True to trigger alarm'''
        if current_value > self.threshold:
            self.triggered = True
            return True
        else:
            return False
      
    def __str__(self):
        '''Print alarm message'''
        return (
            f"{self.alarm_type.upper()} > {self.threshold}% "
            f"{'WARNING ALARM TRIGGERED' if self.triggered else ''}"
        )

