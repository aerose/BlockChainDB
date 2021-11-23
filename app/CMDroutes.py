import argparse
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
from fuzzywuzzy import process
import click
import sys


from app.blockChain import *
from app.routes import mng

target = mng
wordList1 = ['use', 'create', 'delete', 'help', 'showall', 'quit']
wordList2 = ['find', 'add', 'revoke', 'help', 'quit']
completer1 = WordCompleter(wordList1, ignore_case=True)
completer2 = WordCompleter(wordList2, ignore_case=True)


class CMDroutes:
    @staticmethod
    def page1():
        while 1:
            user_input = prompt(str(target.bc) + '>',
                                history=FileHistory(
                                    'app/chain_data/history.txt'),
                                auto_suggest=AutoSuggestFromHistory(),
                                completer=completer1,
                                )
            cmd = user_input.split(" ")
            if cmd[0] == 'help':
                print('''
    simple BlockChain DataBase Operation Index
                    
    use <DBname>        select the database
    create <DBname>     create a database
    delete <DBname>     delete a database
    showall             show all database names
    q or quit           quit 

                    ''')
            elif cmd[0] == 'use':
                tar = user_input.replace('use', '', 1)
                tar = tar.lstrip()
                if tar == '':
                    print("please enter the name")
                else:
                    if target.use(tar):
                        break
                    else:
                        print('cant find')
            elif cmd[0] == 'create':
                tar = user_input.replace('create', '', 1)
                tar = tar.lstrip()
                if tar == '':
                    print("please enter the name")
                else:
                    if target.list_add(tar):
                        print('create successfully')
                    else:
                        print('cant create')
            elif cmd[0] == 'delete':
                tar = user_input.replace('delete', '', 1)
                tar = tar.lstrip()
                if tar == '':
                    print("please enter the name")
                else:
                    if target.delete(tar):
                        print('delete successfully')
                    else:
                        print('cant delete')
            elif cmd[0] == 'showall':
                print('available database:\n' + mng.showDB())
            elif cmd[0] == 'q' or cmd[0] == 'quit':
                mng.strg()
                sys.exit(0)
            else:
                print(str(cmd[0]) + ': command not found')
                print('Maybe you want to use the following instructions:')
                print(process.extract(cmd[0], wordList1, limit=2))
                print('enter help for more details')

    @staticmethod
    def page2():
        while 1:
            user_input = prompt(str(target.bc) + '>',
                                history=FileHistory('app/chain_data/history.txt'),
                                auto_suggest=AutoSuggestFromHistory(),
                                completer=completer2,
                                )
            cmd = user_input.split(" ")
            if cmd[0] == 'help':
                print('''
    simple BlockChain DataBase Operation Index
                    
    find <str> [-v]     select the msg(<*> to show all)(-v or --verbose show in verbose way)
    add <str>           insert a new msg
    revoke              revoke the latest insert
    q or quit           logout 

                    ''')
            elif cmd[0] == 'find':
                tar = user_input.replace('find', '', 1)
                tar = tar.lstrip()
                if tar == '':
                    print("please enter the msg")
                elif cmd[-1] == '-v':
                    tar = tar[0:-3]
                    click.echo_via_pager(target.bc.find(tar))
                elif cmd[-1] == '--verbose':
                    tar = tar[0:-10]
                    click.echo_via_pager(target.bc.find(tar))
                else:
                    click.echo_via_pager(target.bc.spFind(tar))
            elif cmd[0] == 'add':
                tar = user_input.replace('add', '', 1)
                tar = tar.lstrip()
                if tar == '':
                    print("please enter the msg")
                else:
                    target.bc.new_data(tar)
                    target.bc.new_block()
                    print('add successfully')
            elif cmd[0] == 'revoke':
                if target.bc.revoke():
                    print('fin')
            elif cmd[0] == 'q' or cmd[0] == 'quit':
                mng.strg()
                mng.bc = blockChain('BCDB')
                print("fin")
                break
            else:
                print(str(cmd[0]) + ': command not found')
                print('Maybe you want to use the following instructions:')
                print(process.extract(cmd[0], wordList2, limit=2))
                print('enter help for more details')

    @staticmethod
    def run(args):
        use = args.use
        if use:
            target.use(use)
        while 1:
            if mng.bc.name == 'BCDB':
                CMDroutes.page1()
            CMDroutes.page2()
        mng.strg()

    @staticmethod
    def BCDB_args():
        parser = argparse.ArgumentParser(
            description='simple BlockChain DataBase')
        parser.add_argument('-u', '--use',
                            type=str, help='DB to use')
        parser.add_argument('-v', '--version', action='version',
                            version='Simple BlockChain DataBase CMD server 1.0')
        return parser.parse_args()
