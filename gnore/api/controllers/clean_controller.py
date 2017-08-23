from cement.core.controller import CementBaseController, expose
from gnore.api.services import gnore_service

class CleanController(CementBaseController):
    class Meta:
        label = 'clean'
        description = 'Clean files listed in .gitignore'
        stacked_on = 'base'
        stacked_type = 'nested'
        arguments = [
            (['-n', '--nuke'], {
                'action': 'store_true',
                'dest': 'nuke',
                'help': 'Nuke all files'
            }),
            (['-v', '--verbose'], {
                'action': 'store_true',
                'dest': 'verbose',
                'help': 'Verbose'
            })
        ]

    @expose(hide=True)
    def default(self):
        pargs = self.app.pargs
        return gnore_service.clean(
            nuke=pargs.nuke,
            verbose=pargs.verbose
        )
