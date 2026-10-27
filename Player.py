from CollideObjectBase import SphereCollideObject
from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task

class Spaceship(SphereCollideObject):
    def __init__(self, loader: Loader, taskMgr: TaskManager, accept: Callable[[str, Callable], None], modelPath:str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scalevec: float):
        super().__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.taskMgr = taskMgr
        self.accept = accept
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scalevec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self. modelNode.setTexture(tex, 1)

        self.taskManager = taskMgr
        self.accept = accept
        self.render = parentNode
        self.SetKeyBindings()

    def SetKeyBindings(self):
        # All of out key bindings for our spaceship's movement
        self.accept('space', self.Thrust, [1])
        self.accept('space-up', self.Thrust, [0])
        self.accept('arrow_left', self.LeftTurn, [1])
        self.accept('arrow_left-up', self.LeftTurn, [0])
        self.accept('arrow_right', self.RightTurn, [1])
        self.accept('arrow_right-up', self.RightTurn, [0])
        self.accept('arrow_up', self.UpTurn, [1])
        self.accept('arrow_up-up', self.UpTurn, [0])
        self.accept('arrow_down', self.DownTurn, [1])
        self.accept('arrow_down-up', self.DownTurn, [0])
        self.accept('q', self.RollLeft, [1])
        self.accept('q-up', self.RollLeft, [0])
        self.accept('e', self.RollRight, [1])
        self.accept('e-up', self.RollRight, [0])
        
    def LeftTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyLeftTurn, 'left-turn')
        else:
            self.taskManager.remove('left-turn')
    
    def ApplyLeftTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont
    
    def RightTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRightTurn, 'right-turn')
        else:
            self.taskManager.remove('right-turn')
    
    def ApplyRightTurn(self, task):
        rate = .5
        self.modelNode.setH(self.modelNode.getH() - rate)
        return Task.cont
    
    def UpTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyUpTurn, 'up-turn')
        else:
            self.taskManager.remove('up-turn')
    
    def ApplyUpTurn(self, task):
        rate = .5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont
    
    def DownTurn(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyDownTurn, 'down-turn')
        else:
            self.taskManager.remove('down-turn')
    
    def ApplyDownTurn(self, task):
        rate = .5
        self.modelNode.setP(self.modelNode.getP() - rate)
        return Task.cont
    
    def RollLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollLeft, 'roll-left')
        else:
            self.taskManager.remove('roll-left')
    
    def ApplyRollLeft(self, task):
        rate = .5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
    
    def RollRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyRollRight, 'roll-right')
        else:
            self.taskManager.remove('roll-right')
    
    def ApplyRollRight(self, task):
        rate = .5
        self.modelNode.setR(self.modelNode.getR() - rate)
        return Task.cont
    
    def Thrust(self, keyDown):
        if keyDown:
            self.taskManager.add(self.ApplyThrust, 'forward-thrust')
        else:
            self.taskManager.remove('forward-thrust')
    
    def ApplyThrust(self, task):
        rate = 5
        trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
