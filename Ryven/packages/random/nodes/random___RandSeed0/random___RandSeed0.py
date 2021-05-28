from NENV import *


# API METHODS

# self.main_widget()        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# self.set_output_val(index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# ------------------------------------------------------------------------------

import random


class RandSeed_Node(Node):
    def __init__(self, params):
        super(RandSeed_Node, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, inp=-1):
        if inp == 0:
            random.seed(self.input(1))
            self.exec_output(0)

    def get_state(self):
        data = {}
        # ...
        return data

    def set_state(self, data):
        pass # ...

    def removing(self):
        pass