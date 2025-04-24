"""
        bill : مصفوفة تحتوي على أسعار جميع الأصناف التي تم طلبها
        k    : فهرس العنصر (بالترتيب من الصفر) الذي لم تأكله آنا
        b    : المبلغ الذي دفعته آنا بعد أن حسبه براين.
"""

def bonAppetit(bill, k, b):
    s = sum(bill)
    charges = ( s-  bill[k]) // 2
    if b == charges:
        print("Bon Appetit")
    else:
        print(b - charges)
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
