#Реализовать класс автомобиль с полями: объем бака, количество бензина, текущий расход бензина(?),
#текущий объем бензина и скорость движения.
# Реализовать методы: старт, разгон, торможение и остановка

class MyCar():
    def __init__(self, max_petrol_volume, current_petrol_volume, max_speed, current_speed, current_consumption,
                 start_time, stop_time):
        self.max_petrol_volume = max_petrol_volume
        self.current_petrol_volume = current_petrol_volume
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.current_consumption = current_consumption
        self.start_time = start_time
        self.stop_time = stop_time


    def get_current_consumption(self):
        print("Расход бензина к настоящему моменту составил (л): " + str(self.current_consumption))

    def get_current_petrol_volume(self):
        self.current_petrol_volume -= self.current_consumption
        print("Объем бензина в баке к настоящему моменту составил (л): " + str(self.current_petrol_volume))

    def start(self):
        self.current_consumption += 0.05

    def stop(self, ):
        self.current_consumption += 0.025
        self.current_speed = 0

    # def consumption_velocity_dependence(self):
    #     if self.current_speed > 0 and self.current_speed <= 10:
    #         self.current_consumption = 10
    #     elif self.current_speed > 10 and self.current_speed <= 20:
    #         self.current_consumption = 9.5
    #     elif self.current_speed > 20 and self.current_speed <= 30:
    #         self.current_consumption = 9
    #     elif self.current_speed > 30 and self.current_speed <= 40:
    #         self.current_consumption = 8.5
    #     elif self.current_speed > 40 and self.current_speed <= 50:
    #         self.current_consumption = 8
    #     elif self.current_speed > 50 and self.current_speed <= 60:
    #         self.current_consumption = 7.5
    #     elif self.current_speed > 60 and self.current_speed <= 70:
    #         self.current_consumption = 7
    #     elif self.current_speed > 70 and self.current_speed <= 80:
    #         self.current_consumption = 6.5
    #     elif self.current_speed > 80 and self.current_speed <= 90:
    #         self.current_consumption = 6
    #     elif self.current_speed > 90 and self.current_speed <= 100:
    #         self.current_consumption = 5.5
    #     else: self.current_consumption = 5
    #     return self.current_consumption


    def func(self, distance_dict, speed_dict, cons_dict, distance=0):
        time = self.start_time + self.stop_time
        for key in distance_dict.keys():
            if distance < 30:
                distance += distance_dict[key]
                if speed_dict[key] > self.max_speed:
                    self.current_speed = self.max_speed
                else:
                    self.current_speed = speed_dict[key]
                time += (distance_dict[key]/self.current_speed)*60
                self.current_consumption += cons_dict[self.current_speed]*distance_dict[key]/100
        print("Суммарное время в пути (с учетом времени на разгорев и останов) составило (мин): " + str(round(time, 2)))


dict1 = {1: 2, 2: 3, 3: 5, 4: 5, 5: 5, 6: 4, 7: 4, 8: 2, 9: 5, 10: 5, 11: 3, 12: 5, 13: 2}
dict2 = {1: 10, 2: 20, 3: 40, 4: 60, 5: 40, 6: 90, 7: 120, 8: 90, 9: 40, 10: 70, 11: 50, 12: 20, 13: 5}
dict3 = {10: 10, 20: 9.5, 30: 9, 40: 8.5, 50: 8, 60: 7.5, 70: 7, 80: 6.5, 90: 6, 100: 5.5, 110: 5}


myCar = MyCar(50, 35, 110, 0, 0, 2, 2.5)
myCar.start()
myCar.func(dict1, dict2, dict3)
myCar.stop()


myCar.get_current_consumption()
myCar.get_current_petrol_volume()











