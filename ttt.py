import numpy as np

class KNearestNeighbor(object):
  """ a kNN classifier with L2 distance """

  def __init__(self):
    pass

  def train(self, X, y):
    """
    ทำการ train k-NN โดยการจำข้อมูลชุด train ทั้งหมด เก็บไว้ในตัวแปร X_train, y_train

    """
    self.X_train = X
    self.y_train = y
    
  def predict(self, X, k=1):
    """
    ทำนาย label ของข้อมูลชุด test

    Inputs:
    - X: ข้อมูลชุด test
    - k: ค่า hyperparameter k ของอัลกอริทึม k-NN

    Returns:
    - y: อาเรย์ของผลการทำนาย label โดยที่ y[i] เก็บผลทำนายของข้อมูลตัวที่ i  
    """
    
    dists = self.compute_distances_two_loops(X)

    return self.predict_labels(dists, k=k)

  def compute_distances_two_loops(self, X):
    """
    คำนวณระยะห่างระหว่างข้อมูลชุดทดสอบทุกตัว กับข้อมูลชุดฝึกทุกตัว

    Inputs:
    - X: ข้อมูลชุดทดสอบ

    Returns:
    - dists: distance matrix ขนาด (num_test, num_train) ซึ่ง dists[i, j]
      จะเก็บระยะห่าง L2 ระหว่าง ith test point กับ the jth training
      point.
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
      for j in range(num_train):
        # TODO: คำนวณหา dists[i,j] (ห้ามใช้ loop เข้าไปในแต่ละมิติของข้อมูล)
        
        pass
        #####################################################################
        #                       END OF YOUR CODE                            #
        #####################################################################
    return dists

  def predict_labels(self, dists, k=1):
    """
    Given a matrix of distances between test points and training points,
    predict a label for each test point.

    Inputs:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      gives the distance betwen the ith test point and the jth training point.

    Returns:
    - y: A numpy array of shape (num_test,) containing predicted labels for the
      test data, where y[i] is the predicted label for the test point X[i].  
    """
    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)
    for i in range(num_test):
      # อาเรย์ขนาด k ซึ่งจะเก็บ k nearest neighbors ของข้อมูลชุด tesst ตัวที่ i
      closest_y = []
      # TODO: ใช้ distance matrix ในการหา k nearest neighbors
      # และใช้ self.y_train ในการหาค่า label เพื่อนบ้าน k ตัวดังกล่าว
      # เก็บคำตอบไว้ใน closest_y
      # hint: ใช้ฟังก์ชัน numpy.argsort ช่วย
    
      pass

      # TODO: หา majority vote ของเพื่อนบ้าน k ตัวแล้วเก็บผลลัพธ์ใน y_pred
      # หากเกิดการเสมอกัน ให้เลือก (prioritize) label ที่มีค่าที่น้อยกว่า

      pass
      #########################################################################
      #                           END OF YOUR CODE                            # 
      #########################################################################

    return y_pred

