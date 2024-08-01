# %%
def reverseBits(n):
    result = 0
    for i in range(8):
        print(f"Iteration {i + 1}:")
        print(f"n (before):     {bin(n)[2:].zfill(8)}")
        print(f"result (before): {bin(result)[2:].zfill(8)}")

        result = (result << 1) | (n & 1)
        n = n >> 1

        print(f"n (after):      {bin(n)[2:].zfill(8)}")
        print(f"result (after):  {bin(result)[2:].zfill(8)}")
        print("---")
    return result


n = 0b10101100  # 172 in decimal
print("Final result:", bin(reverseBits(n))[2:].zfill(8))
