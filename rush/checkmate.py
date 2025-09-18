def check_dimension(board): #check ว่า boradเป็นจตุรัสมั้ย
    col = len(board) #จำนวนแถวแนวตั้ง
    for i in range(len(board)):
        if(col != len(board[i])):# check ว่าเท่ากับrows แนวนอนมั้ย
            return False
    return True

def check_position(b):
    pos = {"Q":[],"B":[],"R" :[],"P":[],"K":[]} #สร้าง dict เก็บพิกัดของหมากแต่ละตัวรวมKingด้วย
    for i in range(len(b)): #ลูปไปในแต่ละแถว
        for j in range(len(b[i])):#ลูปดูข้อมูลในแถวนั้น
            if((b[i][j]) in pos): #ถ้าข้อมูลในแถวนั้นมีอยู่ใน dict เช่น Q,B,R,P,K จะให้ใส่พิกัดที่เจอเพิ่มไปใน list ที่เปน value ของ keyที่เจอ
                pos[(b[i][j])].append((i,j))
    return pos


def pawn_attack(pos):
    pos_atk = [] #สร้าง list เปล่าเพื่อเตรียมคืนค่าให้ฟังชัน
    for i in pos["P"]:#ลูปพิกัดของ Pawn ทุกตัว
        a,b = i
        pos_atk.append((a-1,b-1)) #:ซ้ายบน
        pos_atk.append((a-1,b+1)) # ขวาบน
    return pos_atk

def rook_attack(pos,n,board):
    pos_atk = [] #สร้าง list เปล่าเพื่อเตรียมคืนค่าให้ฟังชัน
    for rook in pos["R"]:#ลูปพิกัดของ Rook ทุกตัว
        a,b = rook
        # เดินขึ้น
        for i in range(a-1,-1,-1):#ลูปเริ่มที่ด้านบนของพิกัดโดยนับถอยหลังไปเรื่อยๆจนกว่าจะสุด
            if board[i][b] in ["R","P","Q","B","K"]: #ขยับขึ้นไปเรื่อยๆ fix แนวตั้งไว้ ถ้าเจอหมากจะคืนค่าถึงหมากตัวนั้นที่ชนและหยุดลูปเพราะจะเดินข้ามหมากไม่ได้
                pos_atk.append((i,b))
                break
            pos_atk.append((i,b))
        # เดินลง
        for i in range(a+1,n):#ลูปเดินลงไปเรื่อยๆจนถึงตัวสุดท้ายของคอลั่ม
            if board[i][b] in ["R","P","Q","B","K"]:#ขยับลงไปเรื่อยๆ fix แนวตั้งไว้ ถ้าเจอหมากจะคืนค่าถึงหมากตัวนั้นที่ชนและหยุดลูปเพราะจะเดินข้ามหมากไม่ได้
                pos_atk.append((i,b))
                break
            pos_atk.append((i,b))
         # เดินซ้าย
        for j in range(b-1, -1, -1):#ลูปทางซ้ายของพิกัดไปเรือยๆจนกว่าจะสุด 
            if board[a][j] in ["R","P","Q","B","K"]:#ขยับซ้ายไปเรื่อยๆ fix แถวไว้ ถ้าเจอหมากจะคืนค่าถึงหมากตัวนั้นที่ชนและหยุดลูปเพราะจะเดินข้ามหมากไม่ได้
                pos_atk.append((a, j))
                break
            pos_atk.append((a, j))
        # เดินขวา
        for j in range(b+1, n):#ลูปเริ่มจากทางขวาของพิกัดไปเรื่่อยๆจนกว่าจะถึงตัวสุดท้่ายของแถว
            if board[a][j] in ["R","P","Q","B","K"]:#ขยับขวาไปเรื่อยๆ fix แถวไว้ ถ้าเจอหมากจะคืนค่าถึงหมากตัวนั้นที่ชนและหยุดลูปเพราะจะเดินข้ามหมากไม่ได้
                pos_atk.append((a, j))
                break
            pos_atk.append((a, j))
    return pos_atk

def bishop_attack(position, n, board):
    pos_atk = [] #สร้าง list เปล่าเพื่อเตรียมคืนค่าให้ฟังชัน
    for a, b in position["B"]:
        # ซ้ายบน
        i, j = a-1, b-1 #ให้เริ่มจาก ซ้ายบนของพิกัด
        while i >= 0 and j >= 0: #ลูปจนกว่าจะเกินสนาม iเลื่อนขึ้นบน j เลื่อนซ้าย
            if board[i][j] in ["R","P","Q","B","K"]:#ถ้าชนกับหมากตัวอื่นให้เก็บพิกัดล่าสุดและหยุดลูป
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i -= 1 #ขยับซ้ายบน
            j -= 1
        # ขวาบน
        i, j = a-1, b+1 #เริ่มจากขวาบน
        while i >= 0 and j < n:#ลูปจนกว่าจะเกินสนาม iเลื่อนขึ้นบน j เลื่อนขวา
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i -= 1
            j += 1
        # ซ้ายล่าง
        i, j = a+1, b-1
        while i < n and j >= 0:#ลูปจนกว่าจะเกินสนาม iเลื่อนลงล่าง j เลื่อนซ้าย
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i += 1
            j -= 1
        # ขวาล่าง
        i, j = a+1, b+1
        while i < n and j < n:#ลูปจนกว่าจะเกินสนาม iเลื่อนลงล่าง j เลื่อนขวา
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i += 1
            j += 1
    return pos_atk
def queen_attack(position, n,board):
    #วิธีเดินคือ Rook + Bishop
    pos_atk = []
    for queen in position["Q"]:
        a,b = queen
        # เดินขึ้น
        for i in range(a-1,-1,-1):
            if board[i][b] in ["R","P","Q","B","K"]:
                pos_atk.append((i,b))
                break
            pos_atk.append((i,b))
        # เดินลง
        for i in range(a+1,n):
            if board[i][b] in ["R","P","Q","B","K"]:
                pos_atk.append((i,b))
                break
            pos_atk.append((i,b))
         # เดินซ้าย
        for j in range(b-1, -1, -1):
            if board[a][j] in ["R","P","Q","B","K"]:
                pos_atk.append((a, j))
                break
            pos_atk.append((a, j))
        # เดินขวา
        for j in range(b+1, n):
            if board[a][j] in ["R","P","Q","B","K"]:
                pos_atk.append((a, j))
                break
            pos_atk.append((a, j))
        # ซ้ายบน
        i, j = a-1, b-1
        while i >= 0 and j >= 0:
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i -= 1
            j -= 1
        # ขวาบน
        i, j = a-1, b+1
        while i >= 0 and j < n:
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i -= 1
            j += 1
        # ซ้ายล่าง
        i, j = a+1, b-1
        while i < n and j >= 0:
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i += 1
            j -= 1
        # ขวาล่าง
        i, j = a+1, b+1
        while i < n and j < n:
            if board[i][j] in ["R","P","Q","B","K"]:
                pos_atk.append((i, j))
                break
            pos_atk.append((i, j))
            i += 1
            j += 1
    return pos_atk
def checkmate(board):
    board_line = board.splitlines() #แยกข้อความของแต่ละแถวจะได้เป็น list ของข้อความแต่ละแถว ex.[...,...,...,]
    board_list = []#list หลัก
    for i in board_line:
        board_list.append(list(i))#ลูปเอาข้อความแต่ละแถวมาครอบด้วยlistแล้วเอาใส่listหลักทำเปน array 2 มิติ ให้หาพิกัดง่ายๆ


    if(check_dimension(board_list)==False): #เรียก function check ว่าเป็นจตุรหัสไหม
       print("Board must be Square")
       return
    
    rows = len(board_list) #จำนวนแถว ถ้าเป็นจตุรหัส rows cols ต้องเท่ากันอยู่แล้ว
    position = check_position(board_list) #เรียก function หา position ของหมากหลักทุกตัว


    if(position["K"] == []): #check ว่า มี kingไหม
        print("No king.")
        return
    

    if(len(position["K"]) > 1):#check ว่า มี king ตัวเดียวไหม
        print("Must have only one king.")
        return
    
    #checkว่าช่องที่หมากแต่ละตัวโจมตีได้โดน king ไหม
    for i in pawn_attack(position):
        if(position["K"][0] == i):
            print("Success")
            return
    for i in rook_attack(position,rows,board_list):
        if(position["K"][0] == i):
            print("Success")
            return
    for i in bishop_attack(position,rows,board_list):
        if(position["K"][0] == i):
            print("Success")
            return
    for i in queen_attack(position,rows,board_list):
        if(position["K"][0] == i):
            print("Success")
            return
    print("Fail")