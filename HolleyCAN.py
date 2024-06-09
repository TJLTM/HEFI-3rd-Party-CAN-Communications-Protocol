import warnings

class Parser():
    def __init__(self, SerialNumber, SubScribedFunctions = 'All'):
        '''
        format CANID to function to parse the data
        because this is just weird ass stuff 
        '''
        
        '''
        From the document the CANId includes the SerialNumber which must be Filtered For 
        '''
        self.__SerialNumber = SerialNumber
        self.__SNMask = '\xff\xff\xf8\x00'

        '''
        Certain Subscriptions need data type specified 
        '''
        self.__Subscriptions = []
        self.__NeedsSpecialAttention = ['1E051','1E055','1E059','1E05D','1E067']
        self.__ValidIODataTypes = {'bool', "duty_cycle", "msec"}
        
        self.__Map = {
            '1E001' : {'Function':self.__RTCAndRPM,'Index':0,},
            '1E005' : {'Function':self.__FuelFLowAndInjector,'Index':1,},
            '1E009' : {'Function':self.__CLStatusAndDutyC,'Index':2,},
            '1E00D' : {'Function':self.__AFRLandCLC,'Index':3,},
            '1E011' : {'Function':self.__TargetAFRAndAFRR,'Index':4,},
            '1E015' : {'Function':self.__IgTimeAndAFRAVE,'Index':5,},
            '1E019' : {'Function':self.__MAPandKtard,'Index':6,},
            '1E01D' : {'Function':self.__MATandTPS,'Index':7,},
            '1E021' : {'Function':self.__BaroAndCTS,'Index':8,},
            '1E025' : {'Function':self.__OilAndVoltage,'Index':9,},
            '1E029' : {'Function':self.__PedalPosAndFuelPress,'Index':10,},
            '1E02D' : {'Function':self.__BoostGearAndRevLimit,'Index':11,},
            '1E031' : {'Function':self.__BoostSpeedAndStage,'Index':12,},
            '1E035' : {'Function':self.__BoostTargetAndTime,'Index':13,},
            '1E039' : {'Function':self.__BoostAndSolenoid,'Index':14,},
            '1E03D' : {'Function':self.__N20S1AndWaterMeth,'Index':15,},
            '1E041' : {'Function':self.__N20S2andS3,'Index':16,},
            '1E045' : {'Function':self.__GearAndN20S4,'Index':17,},
            '1E049' : {'Function':self.__LinePressureAndSpeed,'Index':18,},
            '1E04D' : {'Function':self.__InputShaftSpeedAndLineTemp,'Index':19,},
            '1E051' : {'Function':self.__Input1And2,'Index':20,"DefinedAs":'bool'},
            '1E055' : {'Function':self.__Input3And4,'Index':21,"DefinedAs":'bool'},
            '1E059' : {'Function':self.__Output1AndInput5,'Index':22,"DefinedAs":'bool'},
            '1E05D' : {'Function':self.__Output2And3,'Index':23,"DefinedAs":'bool'},
            '1E067' : {'Function':self.__Output4And5,'Index':24,"DefinedAs":'bool'},
        }

        #GenerateDefaultSubscribeList 
        if SubScribedFunctions == 'All':
            for Key in self.__Map:
                self.__Subscriptions.append(Key)
        else:
            self.__Subscriptions = SubScribedFunctions

    @property
    def SerialNumber(self):
        return self.__SerialNumber

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

    def SetIOParseType(self, IOSub, DataType):
        if IOSub in self.__NeedsSpecialAttention:
            if DataType in self.__ValidIODataTypes:
                self.__Map[IOSub]["DefinedAs"] == DataType
            else: 
                warnings.warn('IOSub::{0} has invalid datatype: {1} ::These are valid:'.format(IOSub,DataType,self.__ValidIODataTypes))
        else:
            warnings.warn("IOSub invalid:: {0} ::These are valid:: {1}".format(IOSub, self.__NeedsSpecialAttention))

    @property
    def IODataType(self,IOSub):
        if IOSub in self.__NeedsSpecialAttention:
            return self.__Map[IOSub]["DefinedAs"]
        else:
            warnings.warn("IOSub property invalid:: {0} ::These are valid:: {1}".format(IOSub, self.__NeedsSpecialAttention))
            return None

    def DataToParse(self,DataPacket):
        pass

    def __FloatConversion(self,Byte):
        '''
        This API uses signed fixed point format
        '''

        Value = Byte/256
        return Value

    def __RTCAndRPM(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'RTC','Upper':'RPM'}

    def __FuelFLowAndInjector(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Injector Pulsewidth','Upper':'Fuel FLow'}

    def __CLStatusAndDutyC(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Closed Loop Status','Upper':'Duty Cycle'}

    def __AFRLandCLC(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'AFR Left','Upper':'Closed Loop Compensation'}

    def __TargetAFRAndAFRR(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Target AFR','Upper':'AFR Right'}

    def __IgTimeAndAFRAVE(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Ignition Timing','Upper':'AFR Average'}

    def __MAPandKtard(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'MAP','Upper':'Knock Retard'}

    def __MATandTPS(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'MAT','Upper':'TPS'}

    def __BaroAndCTS(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Barometric Pressure','Upper':'CTS'}

    def __OilAndVoltage(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Oil Pressure','Upper':'Battery Voltage'}

    def __PedalPosAndFuelPress(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Pedal Position','Upper':'Fuel Pressure'}

    def __BoostGearAndRevLimit(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Boost Gear','Upper':'Main Rev Limit'}

    def __BoostSpeedAndStage(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Boost Speed','Upper':'Boost Stage'}

    def __BoostTargetAndTime(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Target Boost','Upper':'Boost Time'}

    def __BoostAndSolenoid(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Boost Solenoid Duty Cycle','Upper':'Boost'}

    def __N20S1AndWaterMeth(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'N20 Stage 1','Upper':'Water Meth Injection'}

    def __N20S2andS3(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'N20 Stage 3','Upper':'N20 Stage 2'}

    def __GearAndN20S4(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Gear','Upper':'N20 Stage 4'}

    def __LinePressureAndSpeed(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Line Pressure','Upper':'Speed'}

    def __InputShaftSpeedAndLineTemp(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Input Shaft Speed','Upper':'Line Temp'}

    def __Input1And2(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Input 2','Upper':'Input 1'}

    def __Input3And4(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Input 4','Upper':'Input 3'}

    def __Output1AndInput5(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Output 1','Upper':'Input 5'}

    def __Output2And3(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Output 3','Upper':'Output 2'}

    def __Output4And5(self,Data):
        '''
        '''
        ReturnValueNames = {'Lower':'Output 5','Upper':'Output 4'}