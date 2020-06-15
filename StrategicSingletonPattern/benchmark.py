class BenchMark:
    # https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    class __BenchMark:
        def __init__(self,arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self,arg):
        if not BenchMark.instance:
            BenchMark.instance = BenchMark.__BenchMark(arg)
        else:
            BenchMark.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)



