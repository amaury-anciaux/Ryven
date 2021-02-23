from PySide2.QtWidgets import QWidget, QHBoxLayout, QComboBox

from ryvencore import GUI

from .source_code_preview.CodePreview_Widget import CodePreview_Widget
from ui.ui_script import Ui_script_widget


class ScriptUI(QWidget):
    def __init__(self, script):
        super().__init__()

        self.script = script
        
        # UI
        self.ui = Ui_script_widget()
        self.ui.setupUi(self)

        self.script.flow.algorithm_mode_changed.connect(self.flow_alg_mode_changed)
        # self.script.flow_view.viewport_update_mode_changed.connect(self.flow_vp_update_mode_changed)

        self.flow_alg_mode_dropdown = QComboBox()
        self.flow_alg_mode_dropdown.addItem('data-flow')
        self.flow_alg_mode_dropdown.addItem('exec-flow')
        self.ui.settings_groupBox.layout().addWidget(self.flow_alg_mode_dropdown)
        self.flow_alg_mode_dropdown.currentTextChanged.connect(self.flow_algorithm_mode_toggled)

        # catch up on flow modes
        self.flow_alg_mode_changed(self.script.flow.algorithm_mode())
        # self.flow_vp_update_mode_changed(self.script.flow_view.viewport_update_mode())

        # variables list widget
        self.vars_list_widget = GUI.VarsList(self.script.vars_manager)
        self.ui.variables_group_box.layout().addWidget(self.vars_list_widget)
        self.ui.settings_vars_splitter.setSizes([40, 700])

        # flow
        self.ui.splitter.insertWidget(0, self.script.flow_view)

        # code preview
        self.code_preview_widget = CodePreview_Widget(self.script.flow_view)
        self.ui.source_code_groupBox.layout().addWidget(self.code_preview_widget)

        # logs
        self.ui.logs_scrollArea.setWidget(self.create_logs_widget())
        self.ui.splitter.setSizes([700, 0])
        self.script.logger.new_log_created.connect(self.add_log_widget)
        # self.script.logger.create_default_logs()

        # catch up on logs which might have been loaded from a project already
        for log in self.script.logger.logs:
            self.add_log_widget(log)


    def create_logs_widget(self):
        w = QWidget()
        w.setLayout(QHBoxLayout())
        # w.setStyleSheet('')
        return w


    def add_log_widget(self, log):
        self.ui.logs_scrollArea.widget().layout().addWidget(GUI.LogWidget(log))


    def flow_alg_mode_changed(self, mode: str):
        if mode == 'data':
            self.flow_alg_mode_dropdown.setCurrentIndex(0)
        elif mode == 'exec':
            self.flow_alg_mode_dropdown.setCurrentIndex(1)

    
    def flow_algorithm_mode_toggled(self):
        mode = ''
        if self.flow_alg_mode_dropdown.currentIndex() == 0:
            mode = 'data'
        else:
            mode = 'exec'
        self.script.flow.set_algorithm_mode(mode)