from cement.core.controller import CementBaseController, expose

class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Utility for .gitignore'

    @expose(hide=True)
    def default(self):
        return
