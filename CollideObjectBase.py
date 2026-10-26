from panda3d.core import PandaNode, Loader, NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3

class PlacedObject(PandaNode):
    # Just a generic object in the scene at this point. No relation to collisions.
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelNode: NodePath = loader.loadModel(modelPath)

        # We want to make sure we are having the right type passed to this parameter, or else throw an error.
        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject loader.loadModel(" + modelPath + ") did not return a proper PandaNode!")

        self.modelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)
