

import xml.etree.ElementTree as ET


# load from file
# tree = ET.parse('cronograma.planner')
# root = tree.getroot()

# load directly from a string:
# root = ET.fromstring(country_data_as_string)


class PyPlanner():

    def __init__(self, xml_as_string):
        self.root = ET.fromstring(xml_as_string)

    def get_tasks(self):
        tasks_list = []
        for tasks in self.root.iter('tasks'):
            # return
            return self._listar_tareas(tasks,)
            # for child in list(tasks):
            #     task = {'parent-id': False, 'resource-id': self.get_task_resource(child.attrib['id'])}
            #     task.update(child.attrib)
            #     tasks_list.append(task)
            #     for grant_child in list(child):
            #         child_task = {}
            #         if grant_child.attrib:
            #             child_task['parent-id'] = child.attrib['id']
            #             child_task['resource-id'] = self.get_task_resource(grant_child.attrib['id'])
            #             child_task.update(grant_child.attrib)
            #             tasks_list.append(child_task)
            # return tasks_list

    def _listar_tareas(self, element, parent_id=False, tasks_list = []):
        for e in list(element):
            # if 'predecessor-id' in e.attrib or 'predecessors' in e.attrib:
            #     continue
            if str(e.tag) == 'task':
                if len(list(e)) > 0:
                    # print(';+' + str(e.attrib))
                    e.attrib.update({'parent_id': parent_id})
                    e.attrib.update({'resource_id': self.get_task_resource(e.attrib['id'])})
                    tasks_list.append(e.attrib)
                    self._listar_tareas(e, parent_id=e.attrib['id'], tasks_list=tasks_list)
                else:
                    e.attrib.update({'parent_id': parent_id})
                    e.attrib.update({'resource_id': self.get_task_resource(e.attrib['id'])})
                    tasks_list.append(e.attrib)
        return tasks_list


    def get_resources(self):
        resources_list = []
        for resources in self.root.iter('resources'):
            for child in list(resources):
                resources_list.append(child.attrib)
        return resources_list

    def get_task_resource(self, task_id):
        # TODO: binary search is more efficient
        for allocation in self.root.iter('allocations'):
            resource_list = []
            for child in list(allocation):
                if child.attrib['task-id'] == task_id:
                    resource_list.append(child.attrib['resource-id'])
            return resource_list


