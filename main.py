# =====================================================
#  main.py — ศูนย์กลางของระบบ (งานของหัวหน้ากลุ่ม!)
#
#  เมนู 1 และ 2 เขียนให้ดูเป็นตัวอย่างแล้ว
#  หน้าที่ของหัวหน้า: เขียนเมนู 3-6 โดยเรียกใช้ฟังก์ชันที่เพื่อนเขียน
#  pattern เดียวกันทุกเมนู:  รับ input -> เรียกฟังก์ชัน -> print ผลลัพธ์
# =====================================================
from data import weapons_catalog
from personnel.add_member import add_member
from personnel.show_members import show_members
from personnel.search_member import search_member
from personnel.remove_member import remove_member
from weapon_shop.show_catalog import show_catalog
from weapon_shop.equip_item import equip_item
from missions.send_mission import send_mission

def main():
    while True:
        print("\n=== MAFIA MANAGEMENT SYSTEM ===")
        print("1. รับลูกน้องใหม่")
        print("2. ดูรายชื่อแก๊ง")
        print("3. ค้นหาประวัติ")
        print("4. สั่งเก็บลูกน้อง")
        print("5. คลังอาวุธ")
        # print("6. ส่งไปทำภารกิจ")
        print("6. ออกจากระบบ")

        choice = input("เลือกคำสั่ง (1-6): ")

        # ---------- เมนู 1 (ตัวอย่าง เขียนให้ดูแล้ว) ----------
        if choice == '1':
            print("\n--- เพิ่มลูกน้องใหม่ ---")
            name = input("ชื่อ: ")
            age = int(input("อายุ: "))
            power = int(input("ความโหด (1-10): "))
            money = float(input("เงินส่วย: "))

            new_member = add_member(name, age, power, money)

            if new_member is None:
                print("!! add_member ยังไม่ถูกเขียน (ไปเขียนใน personnel/add_member.py)")
            else:
                print(f"เพิ่ม {new_member['name']} ในตำแหน่ง {new_member['role']} เรียบร้อยแล้ว")

        # ---------- เมนู 2 (ตัวอย่าง เขียนให้ดูแล้ว) ----------
        elif choice == '2':
            print("\n--- รายชื่อลูกน้องทั้งหมด ---")
            show_members()

        # ---------- เมนู 3 (TODO) ----------
        elif choice == '3':
            print("\n--- ค้นหาประวัติ ---")
            # TODO:
            target_name = input("ชื่อที่ต้องการค้นหา : ")
            print(search_member(target_name))
            # print("!! เมนูนี้ยังไม่ถูกเชื่อม")

        # ---------- เมนู 4 (TODO) ----------
        elif choice == '4':
            print("\n--- สั่งเก็บลูกน้อง ---")
            # TODO:
            # 1) รับชื่อคนที่ต้องการลบด้วย input()
            # 2) เรียก remove_member(ชื่อ) แล้วเก็บผลไว้ (ได้ True หรือ False)
            # 3) True  -> print สั่งเก็บเรียบร้อย
            #    False -> print "ไม่พบชื่อในระบบ"
            target_name = input("ชื่อที่ต้องการกำจัดทิ้ง : ")
            remove_member(target_name)
            # print("!! เมนูนี้ยังไม่ถูกเชื่อม")

        # ---------- เมนู 5 (TODO) ----------
        elif choice == '5':
            print("\n=== คลังอาวุธ ===")
            # TODO:
            # 1) เรียก show_catalog() แสดงรายการอาวุธ
            # 2) รับรหัสอาวุธ แล้วหาอาวุธด้วย weapons_catalog.get(รหัส)
            #    (.get(key) เหมือน dict[key] แต่ถ้าไม่มี key นี้จะได้ None แทนที่จะ error)
            #    ถ้าได้ None -> print "ไม่มีสินค้านี้ในระบบ" (จบเมนูนี้เลย)
            # 3) รับชื่อลูกน้อง แล้วหาคนด้วย search_member(ชื่อ)
            #    ถ้าได้ None -> print "ไม่พบรายชื่อลูกน้องคนนี้" (จบเมนูนี้เลย)
            # 4) เรียก equip_item(คน, อาวุธ) แล้วเก็บผลไว้ (ได้ dict)
            #    print ผล["message"]
            #    และถ้าผล["status"] เป็น True -> print ค่าพลังใหม่ของคนนั้น
            show_catalog()
            # print("!! เมนูนี้ยังไม่ถูกเชื่อม")

        # ---------- เมนู 6 (TODO ของหัวหน้า — OPTIONAL) ----------
        # elif choice == '6':
        #     print("\n--- ส่งไปทำภารกิจ ---")
            # TODO:
            # 1) รับชื่อลูกน้อง แล้วหาคนด้วย search_member(ชื่อ)
            #    ถ้าได้ None -> print "ไม่พบรายชื่อลูกน้องคนนี้ในระบบ" (จบเมนูนี้เลย)
            # 2) เรียก send_mission(คน) แล้วเก็บผลไว้ (ได้ dict)
            # 3) ถ้าผล["status"] เป็น True -> print ภารกิจสำเร็จ + เงินรางวัล + ยอดเงินปัจจุบัน
            #    ถ้าเป็น False -> เรียก remove_member(คน["name"]) แล้ว print ภารกิจล้มเหลว ถูกลบออกจากแฟมิลี่
            
            # print("!! เมนูนี้ยังไม่ถูกเชื่อม")

        elif choice == '6':
            print("ปิดระบบ...")
            break
        else:
            print("คำสั่งไม่ถูกต้อง")

if __name__ == "__main__":
    main()
