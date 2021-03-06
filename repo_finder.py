import dropdown, os, fnmatch
class FilteredDirDropdown(dropdown.DropdownView):
    def __init__(self,frame=(0,0,300,32),name='dropdown', filter='*',base=os.path.expanduser('~/Documents'), icloud=False, exclude='.Trash'):
        self.frame=frame
        self.filter=filter
        self.base=base
        self.icloudpath='/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents'
        self.icloud=icloud
        self.exclude=exclude
        super(type(self),self).__init__(
                   frame=frame, 
                   name=name, 
                   items=self.path_generator)

        
    def path_generator(self):
        for rootpath,dirs,_ in os.walk(self.base):
            for d in dirs:
                if self.abort():
                    return
                if fnmatch.fnmatch(d,self.filter) and self.exclude not in rootpath:
                    yield os.path.relpath(rootpath,self.base)
        if self.icloud:
            for rootpath,dirs,_ in os.walk(self.icloudpath):
                for d in dirs:
                    if self.abort():
                        return
                    if fnmatch.fnmatch(d,self.filter) and self.exclude not in rootpath:
                        yield os.path.relpath(rootpath,self.icloudpath)
