import asyncio
import websockets
import random

def calculate_move(col):
    current_player = 1
    best_moves = []
    # Creating the board
    board = [[0 for _ in range(7)] for _ in range(6)]
    # Player 1's play by updating the board.
    for row in range(5, -1, -1):
           if board[row][col] == 0:
               board[row][col] = current_player
               break
    # AI makes a move and checks whether or not the row is filled up
    ai = random.randint(0,6)
    for row in range(5, -1, -1):
        if board[row][ai] == 0:
            ai_row = ai
            break
    return ai_row

async def gameloop (socket, created):
  active = True

  while active:
    message = (await socket.recv()).split(':')
    print(message)

    match message[0]:
      case 'GAMESTART':
        await socket.send('PLAY:3')  
      case 'OPPONENT':
        col = col = calculate_move(int(message[1]))

        await socket.send(f'PLAY:{col}')
      case 'WIN' | 'LOSS' | 'DRAW' | 'TERMINATED':
        print(message[0])

        active = False

async def create_game (server):
  async with websockets.connect(f'ws://128.113.139.63:5000/create') as socket:
    await gameloop(socket, True)

async def join_game(server, id):
  async with websockets.connect(f'ws://128.113.139.63:5000/join/{id}') as socket:
    await gameloop(socket, False)

if __name__ == '__main__':
  server = input('Server IP: ').strip()

  protocol = input('Join game or create game? (j/c): ').strip()

  match protocol:
    case 'c':
      asyncio.run(create_game(server))
    case 'j':
      id = input('Game ID: ').strip()

      asyncio.run(join_game(server, id))
    case _:
      print('Invalid protocol!')