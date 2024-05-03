import warnings

class Parser():
    def __init__(self, SubScribedFunctions = 'All'):
        '''
        format CANID to function to parse the data
        because this is just weird ass stuff 
        '''
        self.__Subscriptions = []
        self.__Map = {
            '1E001000' : {'Function':self.__RTCAndRPM,'Index':0,},
            '1E005000' : {'Function':self.__FuelFLowAndInjector,'Index':1,},
            '1E009000' : {'Function':self.__CLStatusAndDutyC,'Index':2,},
            '1E00D000' : {'Function':self.__AFRLandCLC,'Index':3,},
            '1E011000' : {'Function':self.__TargetAFRAndAFRR,'Index':4,},
            '1E015000' : {'Function':self.__IgTimeAndAFRAVE,'Index':5,},
            '1E019000' : {'Function':self.__MAPandKtard,'Index':6,},
            '1E01D000' : {'Function':self.__MATandTPS,'Index':7,},
            '1E021000' : {'Function':self.__BaroAndCTS,'Index':8,},
            '1E025000' : {'Function':self.__OilAndVoltage,'Index':9,},
            '1E029000' : {'Function':self.__PedalPosAndFuelPress,'Index':10,},
            '1E02D000' : {'Function':self.__BoostGearAndRevLimit,'Index':11,},
            '1E031000' : {'Function':self.__BoostSpeedAndStage,'Index':12,},
            '1E035000' : {'Function':self.__BoostTargetAndTime,'Index':13,},
            '1E039000' : {'Function':self.__BoostAndSolenoid,'Index':14,},
            '1E03D000' : {'Function':self.__N20S1AndWaterMeth,'Index':15,},
            '1E041000' : {'Function':self.__N20S2andS3,'Index':16,},
            '1E045000' : {'Function':self.__GearAndN20S4,'Index':17,},
            '1E049000' : {'Function':self.__LinePressureAndSpeed,'Index':18,},
            '1E04D000' : {'Function':self.__InputShaftSpeedAndLineTemp,'Index':19,},
            '1E051000' : {'Function':self.__Input1And2,'Index':20,},
            '1E055000' : {'Function':self.__Input3And4,'Index':21,},
            '1E059000' : {'Function':self.__Output1AndInput5,'Index':22,},
            '1E05D000' : {'Function':self.__Output2And3,'Index':23,},
            '1E067000' : {'Function':self.__Output4And5,'Index':24,},
        }

        #GenerateDefaultSubscribeList 
        if SubScribedFunctions == 'All':
            for Key in self.__Map:
                self.__Subscriptions.append(Key)
        else:
            self.__Subscriptions = SubScribedFunctions

        

    @property
    def Subscriptions(self):
        return self.__Subscriptions

    def AddSubscription(self,Data):
        if Data in self.__Map.keys():
            self.__Subscriptions.append(Data)
        else:
            warnings.warn("Subscription:{} is not available".format(Data)) 

    def RemoveSubscription(self,Data):
        if Data in self.__Subscriptions:
            self.__Subscriptions.remove(Data)
        else:
            warnings.warn("Not Subscribed: {}".format(Data))

    def DataToParse(self,DataPacket):
        pass

    def __RTCAndRPM(self,Data):
        pass

    def __FuelFLowAndInjector(self,Data):
        pass

    def __CLStatusAndDutyC(self,Data):
        pass

    def __AFRLandCLC(self,Data):
        pass

    def __TargetAFRAndAFRR(self,Data):
        pass

    def __IgTimeAndAFRAVE(self,Data):
        pass

    def __MAPandKtard(self,Data):
        pass

    def __MATandTPS(self,Data):
        pass

    def __BaroAndCTS(self,Data):
        pass

    def __OilAndVoltage(self,Data):
        pass

    def __PedalPosAndFuelPress(self,Data):
        pass

    def __BoostGearAndRevLimit(self,Data):
        pass

    def __BoostSpeedAndStage(self,Data):
        pass

    def __BoostTargetAndTime(self,Data):
        pass

    def __BoostAndSolenoid(self,Data):
        pass

    def __N20S1AndWaterMeth(self,Data):
        pass

    def __N20S2andS3(self,Data):
        pass

    def __GearAndN20S4(self,Data):
        pass

    def __LinePressureAndSpeed(self,Data):
        pass

    def __InputShaftSpeedAndLineTemp(self,Data):
        pass

    def __Input1And2(self,Data):
        pass

    def __Input3And4(self,Data):
        pass

    def __Output1AndInput5(self,Data):
        pass

    def __Output2And3(self,Data):
        pass

    def __Output4And5(self,Data):
        pass