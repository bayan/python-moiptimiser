Minimize multi-objectives

OBJ1: Priority=4 Weight=1 AbsTol=0 RelTol=0
  715 X2_1
 +   715 X1_2
 +   419 X3_1
 +   419 X1_3
 +   289 X4_1
 +   289 X1_4
 +  1060 X5_1
 +  1060 X1_5
 +   385 X6_1
 +   385 X1_6
 +   745 X3_2
 +   745 X2_3
 +   919 X4_2
 +   919 X2_4
 +   889 X5_2
 +   889 X2_5
 +   646 X6_2
 +   646 X2_6
 +   320 X4_3
 +   320 X3_4
 +   686 X5_3
 +   686 X3_5
 +    99 X6_3
 +    99 X3_6
 +  1004 X5_4
 +  1004 X4_5
 +   362 X6_4
 +   362 X4_6
 +   681 X6_5
 +   681 X5_6

OBJ2: Priority=3 Weight=1 AbsTol=0 RelTol=0
 1080 X2_1
 +  1080 X1_2
 +   623 X3_1
 +   623 X1_3
 +   663 X4_1
 +   663 X1_4
 +   497 X5_1
 +   497 X1_5
 +   607 X6_1
 +   607 X1_6
 +   723 X3_2
 +   723 X2_3
 +   442 X4_2
 +   442 X2_4
 +   883 X5_2
 +   883 X2_5
 +  1034 X6_2
 +  1034 X2_6
 +   546 X4_3
 +   546 X3_4
 +   823 X5_3
 +   823 X3_5
 +   311 X6_3
 +   311 X3_6
 +   459 X5_4
 +   459 X4_5
 +   813 X6_4
 +   813 X4_6
 +   973 X6_5
 +   973 X5_6

OBJ3: Priority=2 Weight=1 AbsTol=0 RelTol=0
  375 X2_1
 +   375 X1_2
 +   809 X3_1
 +   809 X1_3
 +   279 X4_1
 +   279 X1_4
 +   518 X5_1
 +   518 X1_5
 +   647 X6_1
 +   647 X1_6
 +   608 X3_2
 +   608 X2_3
 +   206 X4_2
 +   206 X2_4
 +   168 X5_2
 +   168 X2_5
 +   755 X6_2
 +   755 X2_6
 +   540 X4_3
 +   540 X3_4
 +   478 X5_3
 +   478 X3_5
 +   583 X6_3
 +   583 X3_6
 +   276 X5_4
 +   276 X4_5
 +   555 X6_4
 +   555 X4_6
 +   753 X6_5
 +   753 X5_6

OBJ4: Priority=1 Weight=1 AbsTol=0 RelTol=0
  190 X2_1
 +   190 X1_2
 +   470 X3_1
 +   470 X1_3
 +   480 X4_1
 +   480 X1_4
 +   609 X5_1
 +   609 X1_5
 +   672 X6_1
 +   672 X1_6
 +   648 X3_2
 +   648 X2_3
 +   449 X4_2
 +   449 X2_4
 +   475 X5_2
 +   475 X2_5
 +   743 X6_2
 +   743 X2_6
 +   646 X4_3
 +   646 X3_4
 +   921 X5_3
 +   921 X3_5
 +   520 X6_3
 +   520 X3_6
 +   314 X5_4
 +   314 X4_5
 +   394 X6_4
 +   394 X4_6
 +   699 X6_5
 +   699 X5_6



s.t.
X2_1 + X3_1 + X4_1 + X5_1 + X6_1 = 1
X1_2 + X1_3 + X1_4 + X1_5 + X1_6 = 1
X1_2 + X3_2 + X4_2 + X5_2 + X6_2 = 1
X2_1 + X2_3 + X2_4 + X2_5 + X2_6 = 1
X1_3 + X2_3 + X4_3 + X5_3 + X6_3 = 1
X3_1 + X3_2 + X3_4 + X3_5 + X3_6 = 1
X1_4 + X2_4 + X3_4 + X5_4 + X6_4 = 1
X4_1 + X4_2 + X4_3 + X4_5 + X4_6 = 1
X1_5 + X2_5 + X3_5 + X4_5 + X6_5 = 1
X5_1 + X5_2 + X5_3 + X5_4 + X5_6 = 1
X1_6 + X2_6 + X3_6 + X4_6 + X5_6 = 1
X6_1 + X6_2 + X6_3 + X6_4 + X6_5 = 1
U1 - U2 + 6 X1_2 < 6
U1 - U3 + 6 X1_3 < 6
U1 - U4 + 6 X1_4 < 6
U1 - U5 + 6 X1_5 < 6
U1 - U6 + 6 X1_6 < 6
U2 - U1 + 6 X2_1 < 6
U2 - U3 + 6 X2_3 < 6
U2 - U4 + 6 X2_4 < 6
U2 - U5 + 6 X2_5 < 6
U2 - U6 + 6 X2_6 < 6
U3 - U1 + 6 X3_1 < 6
U3 - U2 + 6 X3_2 < 6
U3 - U4 + 6 X3_4 < 6
U3 - U5 + 6 X3_5 < 6
U3 - U6 + 6 X3_6 < 6
U4 - U1 + 6 X4_1 < 6
U4 - U2 + 6 X4_2 < 6
U4 - U3 + 6 X4_3 < 6
U4 - U5 + 6 X4_5 < 6
U4 - U6 + 6 X4_6 < 6
U5 - U1 + 6 X5_1 < 6
U5 - U2 + 6 X5_2 < 6
U5 - U3 + 6 X5_3 < 6
U5 - U4 + 6 X5_4 < 6
U5 - U6 + 6 X5_6 < 6
U6 - U1 + 6 X6_1 < 6
U6 - U2 + 6 X6_2 < 6
U6 - U3 + 6 X6_3 < 6
U6 - U4 + 6 X6_4 < 6
U6 - U5 + 6 X6_5 < 6


GENERAL
U1
U2
U3
U4
U5
U6
BINARY
X1_2
X1_3
X1_4
X1_5
X1_6
X2_1
X2_3
X2_4
X2_5
X2_6
X3_1
X3_2
X3_4
X3_5
X3_6
X4_1
X4_2
X4_3
X4_5
X4_6
X5_1
X5_2
X5_3
X5_4
X5_6
X6_1
X6_2
X6_3
X6_4
X6_5
END
