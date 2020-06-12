class FilterModule(object):

    def filters(self):
        return {
            'cleanup_device_data': self.cleanup_device_data,
        }

    def cleanup_device_data(self, value):
        site_devices = []
        device = {}
        for each in value:
            device['name'] = each['name']
            device['tenant'] = each['tenant']['slug']
            device['platform'] = each['platform']['name']
            device['serial'] = each['serial']
            device['site'] = each['site']['slug']
            site_devices.append(device)
        
        return site_devices