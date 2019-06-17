from niftynet.network.base_net import BaseNet


class MyNet(BaseNet):
 def __init__(self, num_classes, name='MyNet'):

     super(MyNet, self).__init__(
         num_classes=num_classes, acti_func=acti_func, name=name)

     # network specific property
     self.hidden_features = 10

 def layer_op(self, images, is_training):
     # create layer instances
     conv_1 = ConvolutionalLayer(self.hidden_features,
                                 kernel_size=3,
                                 name='conv_input')

     conv_2 = ConvolutionalLayer(self.num_classes,
                                 kernel_size=1,
                                 acti_func=None,
                                 name='conv_output')

     # apply layer instances
     flow = conv_1(images, is_training)
     flow = conv_2(flow, is_training)

     return flow