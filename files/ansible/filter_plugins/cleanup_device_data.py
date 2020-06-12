class FilterModule(object):

    def filters(self):
        return {
            'cleanup_device_data': self.cleanup_device_data,
        }

    def cleanup_device_data(self, value):
        site_devices = []
        core_devices = []
        access_devices = []
        for each in value:
            core = {}
            access = {}
            if each["device_role"]["name"] == 'core':
                core['name'] = each['name']
                core['tenant'] = each['tenant']['slug']
                core['platform'] = each['platform']['name']
                core['serial'] = each['serial']
                core['site'] = each['site']['slug']
                core_devices.append(core)
            elif each["device_role"]["name"] == 'access':
                access['name'] = each['name']
                access['tenant'] = each['tenant']['slug']
                access['platform'] = each['platform']['name']
                access['serial'] = each['serial']
                access['site'] = each['site']['slug']
                access_devices.append(access)
            else:
                pass
        
        asdf = {"core": core_devices}
        qwert = {"access": access_devices}
        site_devices.append(asdf)
        site_devices.append(qwert)
        return site_devices