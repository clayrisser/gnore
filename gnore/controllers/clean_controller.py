from cement.core.controller import CementBaseController, expose
from services import gnore_service

class CleanController(CementBaseController):
    class Meta:
        label = 'clean'
        description = 'Clean files listed in .gitignore'
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(hide=True)
    def default(self):
        return gnore_service.clean()
