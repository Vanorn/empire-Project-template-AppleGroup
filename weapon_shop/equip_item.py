# =====================================================
#  weapon_shop/equip_item.py — คนรับผิดชอบ: ___________PangPang___________
#  หน้าที่: ซื้อและสวมใส่อาวุธให้ลูกน้อง (เช็คเงื่อนไข 2 อย่างก่อน)
# =====================================================
# equip_item - PangPang

#   - เช็คเงิน: เงินของ person ไม่พอราคา weapon -> ซื้อไม่ได้
#   - เช็คอาวุธ: person มีอาวุธอยู่แล้ว (equipment ไม่ใช่ "ไม่มี") -> ใส่เพิ่มไม่ได้
#   - ผ่านทั้งคู่ -> หักเงิน, เปลี่ยน equipment เป็นชื่ออาวุธ, บวก bonus เข้า power
#   - return {"status": True/False, "message": ข้อความบอกผล}
    # TODO: เขียนโค้ดตรงนี้
    
status = {
    "status": True,
    "message": "Success"
}


    
def equip_item (person, weapon):
    
    if (person["equipment"]) != "ไม่มี": 
        return "Already has an equipment on"
        # pass
    if (person["money"]) < (weapon["price"]) :
        return "You don't have enough money"
        # pass
    (person["money"]) -= (weapon["price"])
    (person["equipment"]) = weapon
    (person["power"]) += (weapon["bonus"])
    return status


# ทดสอบเฉพาะไฟล์ตัวเอง: พิมพ์  python -m weapon_shop.equip_item
if __name__ == "__main__":
    vito = {"name": "Vito", "money": 60000, "power": 5, "equipment": "ไม่มี"}
    gun = {"name": "ปืนพก 9mm", "price": 50000, "bonus": 5}

    print(equip_item(vito, gun))   # ต้องได้ status True
    print(vito)                    # เงินเหลือ 10000, power เป็น 10, equipment เป็นปืน
    print(equip_item(vito, gun))   # ครั้งที่สองต้องได้ "มีอาวุธอยู่แล้ว"
