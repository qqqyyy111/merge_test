import json


class load_data:
    def __init__(self):
        self.data = {}

    def load_json_mt(self, mt_path):
        with open(mt_path) as m:
            mt_json = json.load(m)

        data_list = mt_json['DataList']

        self.data['VirtualMemory'] = []
        self.data['Memory'] = []

        for d in data_list:
            if 'fps' not in self.data:
                self.data['fps'] = []
            self.data['fps'].append(d['AndroidFps']['fps'])

            if 'Jank' not in self.data:
                self.data['Jank'] = []
            self.data['Jank'].append(d['AndroidFps']['Jank'])

            if 'InterFrame' not in self.data:
                self.data['InterFrame'] = []
            self.data['InterFrame'].append(d['AndroidFps']['InterFrame'])

            if 'TimeStamp' not in self.data:
                self.data['TimeStamp'] = []
            self.data['TimeStamp'].append(int(d['TimeStamp']) // 1000)

            if 'AppUsage' not in self.data:
                self.data['AppUsage'] = []
            self.data['AppUsage'].append(d['CpuUsage']['AppUsage'])

            if 'TotalUsage' not in self.data:
                self.data['TotalUsage'] = []
            self.data['TotalUsage'].append(d['CpuUsage']['TotalUsage'])

            if 'AndroidMemoryUsage' in d:
                self.data['Memory'].append(d['AndroidMemoryUsage']['Memory'])

            if 'VirtualMemory' in d:
                if 'VirtualMemory' in d['VirtualMemory']:
                    self.data['VirtualMemory'].append(d['VirtualMemory']['VirtualMemory'])

            if 'GpuUsage' not in self.data:
                self.data['GpuUsage'] = []
            self.data['GpuUsage'].append(d['GpuUsage']['Unilization'])

            if 'BigJank' not in self.data:
                self.data['BigJank'] = []
            self.data['BigJank'].append(d['BigJank']['BigJank'])

        return self.data
