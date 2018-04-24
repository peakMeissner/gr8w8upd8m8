from gr8w8upd8m8 import EventProcessor

class SingleEventProcessor(EventProcessor):
    def __init__(self):
        EventProcessor.__init__(self)
    
    def mass(self, event):
        if event.totalWeight > 1:
            self._events.append(event.totalWeight)
            self.done = True
        
    
    @EventProcessor.weight.getter
    def weight(self):
        if not self._events:
            return 0
        
        return self._events.pop()
    
