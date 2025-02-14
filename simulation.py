import sys
from termcolor import colored
import time
import os



class Simulation:

    def __init__(self, name, log=False):
        self.name = name
        self.log = log
        
    def Create(self):
        self.objects = []
        self.ERROR_TYPES = ["OBJECT_ALREADY_EXISTS", "OBJECT_OUT_OF_BOUNDS", "NEGATIVE_DIMENSIONS"]
        self.ignored_errors = []
        self.warnings = 0
        self.objects_created = 0
        self.objects_deleted = 0
        self.start_time = time.time()

    def Ignore(self, ignored_errortype: str):
        self.ignored_errors.append(ignored_errortype)

    def Raise(self,errortype,error):
        if self.log:
            with open("simulation_log.txt") as f:
                f.write(f"Exitted at time () for: {errortype} {error}")
        else:
            pass
        if errortype not in self.ignored_errors:

            sys.exit(colored(f"An error occurred: {errortype} {error}", "red"))
        else:
            print(colored(f"WARNING: {error}", "yellow"))
            self.warnings += 1

    def dimensions(self, x, y):
        self.x = x
        self.y = y
        if x <= 0 or y <= 0:
            self.Raise("NEGATIVE_DIMENSIONS", "Coordinates cannot be negative or equal to zero")
        else: 
            pass
        
    def Add_Object(self, id: str, coordinates: list):
        if self.objects != []:
            for obj in self.objects:
                if id != obj[0]:
                    if coordinates[0] > self.x or coordinates[1] > self.y or obj[1][0] < 0 or obj[1][1] < 0:
                        self.Raise("OBJECT_OUT_OF_BOUNDS", f"Object {id} cannot be created out of bounds")
                    else:
                        self.objects.append([id, coordinates])
                        self.objects_created+=1
                        break
                else:
                    self.Raise("OBJECT_ALREADY_EXISTS", f"Object {id} already exists in this simulation")
        else:
            self.objects.append([id, coordinates])
            self.objects_created+=1

    def Remove_Object(self, id: str):
        new_objects = []
        for obj in self.objects:
            if obj[0] != id:
                new_objects.append(obj)
            else:
                pass
        self.objects = new_objects
        self.objects_deleted+=1
    
    def Move_Object(self, id: str, xplus: int, yplus: int):
        for obj in self.objects:
            if obj[0] == id:
                #index = self.objects[obj.index()][id.index()]
                obj[1][0] += xplus
                obj[1][1] += yplus
                if obj[1][0] > self.x or obj[1][1] > self.y or obj[1][0] < 0 or obj[1][1] < 0:
                    self.Raise("OBJECT_OUT_OF_BOUNDS", f"Object {obj[0]} is out of bounds")
                break
    def Wait(self, seconds: float, print_out = True):
        if print_out:
            print(colored(f"Waiting {seconds} seconds...", "dark_grey"))
        time.sleep(seconds)
        if print_out:
            print(colored(f"Simulation is continuing", "dark_grey"))

    def Register_Collision(self, id: str):
        coordinates = []
        for obj in self.objects:
            if obj[0] == id:
                coordinates = obj[1]
                break
        for obj in self.objects:
            if obj[0] != id:
                if obj[1] == coordinates:
                    print(f"{obj[0]} collided with {id} at {coordinates}")
                    if self.log:
                        with open("sim_log.txt", "a") as file:
                            file.write(f"\n{obj[0]} collided with {id} at {coordinates}")
                    return True
                else:
                    pass
            else:
                pass

        return False


    def Update(self):
        os.system("cls")
        print(self.objects)
        if self.log:
            with open("sim_log.txt", "a") as file:
                file.write(f"\n{self.objects}")

    def Clear_Log(self):
        with open("sim_log.txt", "a") as file:
            file.write("")
            file.close()

    def Finish(self):
        print(colored(f"Simulation {self.name} finished", "magenta"))
        print(f"Objects: {self.objects}")
        print(f"Number of warnings: {self.warnings}")
        print(f"Objects created: {self.objects_created}")
        print(f"Objects deleted: {self.objects_deleted}")
        print(colored(f"Runtime: {time.time() - self.start_time} seconds", "light_yellow"))
        sys.exit("")

             
        









if __name__ == "__main__":
    sim = Simulation("Simulation", log=True)
    sim.dimensions(500,500)
    sim.Create()
    sim.Add_Object("1", [0,0])
    sim.Add_Object("2", [50,50])
    sim.Add_Object("3", [80, 80])
    for i in range(500):
        sim.Move_Object("1", 10, 10)
        sim.Move_Object("2", 5, 5)
        sim.Move_Object("3", 2, 2)
        sim.Update()
        collision = sim.Register_Collision("2")
        if collision:
            try:
                sim.Finish()
            except:
                break
        sim.Wait(1, print_out=False)

    print("lol")
