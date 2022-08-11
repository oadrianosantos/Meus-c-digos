import struct

def Main():
      Y = True
      arq = open("dados.cod", 'wb')
      while Y == True:
          nome = str(input("Digite o nome: \n")).encode()
          rg = (int(str(input("Digite o RG: \n").replace(".", "").replace("-", ""))))
          cpf = (int(str(input("digite o CPF: \n")).replace(".", "").replace("/","")))
          data = struct.pack('10s Q Q', nome, rg, cpf)
          arq.write(data + b'\n')

          cont = input("Deseja continuar? S ou N")
          if cont == "S" or cont == "s":
              Y = True
          else:
              Y = False

      arq.close()

      arq_1 = open("dados.cod", "rb")
      d = arq_1.read()
      a = d.split(b"\n")
      for i in range(len(a)-1):
          da = struct.unpack("10s Q Q", a[i])
          nome = da[0].decode()
          print(nome, da[1], da[2])
          arq_1.close()

Main()
