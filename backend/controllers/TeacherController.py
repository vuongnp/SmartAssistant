from services.TeacherService import TeacherService
from tools.CheckParameter import CheckParameter
from tools.RandomTool import RandomTool
from configurations.AppConfig import AppConfig


class TeacherController:
    def getTeacher_home_handling(db, username):
        try:
            data = TeacherService.getTeacher_home(db, username)
            if data is None:
                result = {
                    'code': '9995',
                    'message': AppConfig.RESPONSE_CODE[9995],
                    'data': {
                        'id': '',
                        'username': '',
                        'role': '',
                    }
                }
                return result
            else:
                result = {
                    'code': '1000',
                    'message': AppConfig.RESPONSE_CODE[1000],
                    'data': {
                        'id': data['teacher']['id'],
                        'name': data['teacher']['name'],
                        'phone': data['teacher']['phone'],
                        'username': data['teacher']['username'],
                        'email': data['teacher']['email'],
                        'gender': data['teacher']['gender'],
                        'age': data['teacher']['age'],
                        'role': data['teacher']['role'],
                        'avatar': data['teacher']['avatar'],
                        'classes': data['classes']
                    }
                }
                return result
        except Exception as ex:
            print("Exception in TeacherController getTeacher_home_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result

    def addClassroom_handling(db, name, description, schedule, type, duration, username):
        try:
            # if name == '' or duration == '':
            #     result = {
            #         'code': '9995',
            #         'message': AppConfig.RESPONSE_CODE[9995],
            #         'data': {}
            #     }
            #     return result
            if name == '' or duration == '' or name is None or duration is None or schedule is None:
                return CheckParameter.get_result_for_miss_parameter()
            if description is None:
                description = ''
            if type is None:
                type = 'Lý thuyết'
            duration = int(duration)
            id = RandomTool.get_random_id()
            code = RandomTool.get_classroom_code()
            teacher = TeacherService.addClassroom(
                db, id, name, description, schedule, type, duration, code, username)
            result = {'code': '1000',
                      'message': AppConfig.RESPONSE_CODE[1000],
                      'data': {
                          'id': teacher['id'],
                          'name': teacher['name'],
                          'phone': teacher['phone'],
                          'username': teacher['username'],
                          'email': teacher['email'],
                          'gender': teacher['gender'],
                          'age': teacher['age'],
                          'role': teacher['role'],
                          'avatar': teacher['avatar'],
                          'classes': teacher['classes']
                      }
                      }
            return result
        except Exception as ex:
            print("Exception in TeacherController addClassroom_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result

    def updateClassroom_handling(db, id, code, name, description, schedule, type, duration):
        try:
            if name == '' or duration == '':
                result = {
                    'code': '9995',
                    'message': AppConfig.RESPONSE_CODE[9995],
                    'data': {}
                }
                return result
            if name is None or duration is None:
                return CheckParameter.get_result_for_miss_parameter()
            if description is None:
                description = ''
            if schedule is None:
                schedule = ''
            if type is None:
                type = 'Lý thuyết'
            duration = int(duration)
            if id:
                TeacherService.update_classroom_by_id(
                    db, id, name, description, schedule, type, duration)
            else:
                TeacherService.update_classroom_by_code(
                    db, code, name, description, schedule, type, duration)
            result = {'code': '1000',
                      'message': AppConfig.RESPONSE_CODE[1000],
                      'data': {}
                      }
            return result
        except Exception as ex:
            print("Exception in TeacherController updateClassroom_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result

    def deleteClassroom_handling(db, id, username):
        try:
            TeacherService.delete_classroom(db, id, username)
            result = {'code': '1000',
                      'message': AppConfig.RESPONSE_CODE[1000],
                      }
            return result
        except Exception as ex:
            print("Exception in TeacherController deleteClassroom_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result

    def getClassroom_handling(db, id):
        try:
            data = TeacherService.get_classroom(db, id)
            result = {
                'code': '1000',
                'message': AppConfig.RESPONSE_CODE[1000],
                'data': {
                        'id': data['classroom']['id'],
                        'name': data['classroom']['name'],
                        'description': data['classroom']['description'],
                        'schedule': data['classroom']['schedule'],
                        'type': data['classroom']['type'],
                        'mode': data['classroom']['mode'],
                        'duration': data['classroom']['duration'],
                        'code': data['classroom']['code'],
                        'is_learning': data['classroom']['is_learning'],
                        'students': data['students']
                }
            }
            return result
        except Exception as ex:
            print("Exception in TeacherController getClassroom_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result
    
    def getStudent_handling(db, id):
        try:
            data = TeacherService.get_student(db, id)
            result = {
                'code': '1000',
                'message': AppConfig.RESPONSE_CODE[1000],
                'data': {
                        'id': data['id'],
                        'name': data['name'],
                        'phone': data['phone'],
                        'username': data['username'],
                        'email': data['email'],
                        'gender': data['gender'],
                        'age': data['age'],
                        'role': data['role'],
                        'avatar': data['avatar'],
                }
            }
            return result
        except Exception as ex:
            print("Exception in TeacherController getStudent_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result
    

    def deleteStudent_handling(db, id_student, id_class):
        try:
            TeacherService.delete_student(db, id_student, id_class)
            result = {'code': '1000',
                      'message': AppConfig.RESPONSE_CODE[1000],
                      }
            return result
        except Exception as ex:
            print("Exception in TeacherController deleteStudent_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result

    def selectClassMode_handling(db, id, mode):
        try:
            TeacherService.update_classroom_mode(db, id, mode)
            result = {'code': '1000',
                      'message': AppConfig.RESPONSE_CODE[1000],
                      'data': {}
                      }
            return result
        except Exception as ex:
            print("Exception in TeacherController selectClassMode_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result

    def toggleStartFinish_handling(db, id):
        try:
            classroom = TeacherService.update_classroom_status(db, id)
            result = {'code': '1000',
                      'message': AppConfig.RESPONSE_CODE[1000],
                      'data': {
                            'id': classroom['id'],
                            'name': classroom['name'],
                            'description': classroom['description'],
                            'schedule': classroom['schedule'],
                            'type': classroom['type'],
                            'mode': classroom['mode'],
                            'duration': classroom['duration'],
                            'code': classroom['code'],
                            'is_learning': classroom['is_learning']
                        }
                      }
            return result
        except Exception as ex:
            print("Exception in TeacherController toggleStartFinish_handling", ex)
            result = {
                'code': '1001',
                'message': AppConfig.RESPONSE_CODE[1001]
            }
            return result
