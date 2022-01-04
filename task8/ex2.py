#2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import huff

def ex2(string):
    tree = huff.get_tree(string)
    codes = huff.get_code(tree)
    codings_str = huff.coding(string, codes)
    return codings_str

if __name__ == '__main__':
    string = "Code Huffman example"
    res = ex2(string)
    print(f"{string} enc result:\n {res}")