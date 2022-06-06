import asyncio
import discord

app = discord.Client()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")

token = "OTgzMDI0MjM2MjM3MDQxNjk0.Gddn1S.ao0aeTC9o9Y1_r6lDKhYeyNLl4A_ioYVMd4tUs"

import asyncio
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='kr ')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('say "kr <string>", type "kr 사용설명서" (kor) or "kr guidebook" (english) '))
    print('[안녕하세요! Foxbot이 가동되었습니다.]')
    print('kr <명령어>를 사용해 한국어 예문을 받을 수 있습니다')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

##봇명령어 테스

@bot.command()
async def 안녕(ctx):
    await ctx.send("{} 나도 안녕!".format(ctx.author.mention))

## 이건 테스트 임베디드
@bot.command()
async def 임베디드(ctx):
    embed = discord.Embed(title="제목", description="설명 ㄴㅇㄹㄴㄹㄴㄹ", color=0x0048ba)
    embed.add_field(name="안녕하세요", value="ㄹㅇㄹㄹㅇㄹㅇ 안녕!", inline=False)
    await ctx.send(embed=embed)

##진짜 임베디드 시작
@bot.command()
async def 소개(ctx):
    embed = discord.Embed(title="폭스봇 소개", description="제가 절 소개해보려고 해요!", color=0x0048ba)
    embed.add_field(name="안녕하세요!", value="폭스봇은 한국어 예문들을 난이도별로 나누어 볼 수 있게 한 디스코드 봇입니다.", inline=False)
    embed.add_field(name="탄생배경", value="이거 만든 사람은 '한중일 언어 배우기 서버'에서 관리자로 활동하고 있는데, 중국어와 일본어 봇은 있는데 한국어 봇은 너무 없는거예요. 그렇다고 제작자는 프로그래밍을 접하지도 못했고... 그래서 고민고민 끝에 직접 봇을 만들게 되었고, 머리를 부여잡으며 6시간동안이나 프로그래밍을 하다가 기초적인 걸 완성했어요. \n 그게 저예요. 헤헤!", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 질문(ctx):
    embed = discord.Embed(title="폭스봇 소개", description="제가 절 소개해보려고 해요!", color=0x0048ba)
    embed.add_field(name="안녕하세요!", value="폭스봇은 한국어 예문들을 난이도별로 나누어 볼 수 있게 한 디스코드 봇입니다.", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def 사용설명서(ctx):
    embed = discord.Embed(title="사용설명서", description="폭스봇 사용설명서", color=0x0048ba)
    embed.add_field(name="kr <명령어>", value='제 접두사는 "kr (명령어)" 예요. 사용설명서에 있는대로 움직일게요. \n"시키면 해야죠!" -건설로봇, 스타크래프트2', inline=False)
    embed.add_field(name="kr 소개", value="제 소개를 할게요. 그런데 쓸데없는 정보가 많답니다.", inline=False)
    embed.add_field(name="kr 질문", value="자주 물을만한 질문들을 모아봤어요.", inline=False)
    embed.add_field(name="난이도?", value="난이도는 1부터 10까지 있어요. 그리고 진짜 어려운 'X' 단계도 있어요! (kr <장르> X) 한번 도전해보시겠어요? :fire: :rooster: :ramen:", inline=False)
    embed.add_field(name="kr 소설 (난이도)", value="레벨에 맞는 소설 지문 일부를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
    embed.add_field(name="kr 시 (난이도)", value="레벨에 맞는 시를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
    embed.add_field(name="kr (장르) 번호 (숫자)", value="지정한 글을 DM으로 보내드려요. DM으로 보내진 모든 글 하단에는 고유 번호가 있는데, 좋아하는 글을 다시 보고 싶으시다면 그 숫자를 기록해주셔도 좋아요!", inline=False)
    embed.add_field(name="kr 모든 (장르)", value="지정한 글 종류가 총 몇 개 수록되어있는 지 알려드려요!", inline=False)
    embed.add_field(name="kr 수필", value="폭스봇 주인이 자기 생각을 적은 노트가 있는데 그 중에서 아무거나 한 장을 뜯어서 뽑아 DM으로 보내드려요! ㅋㅋㅋㅋㅋㅋ", inline=False)
    embed.set_footer(text="다들 한국어 열심히 배워봐요! 화이팅!")
    await ctx.send(embed=embed)

@bot.command()
async def 테스트(ctx):
    embed = discord.Embed(title="너에게 묻는다", description="안도현", color=0x0048ba)
    embed.add_field(name="본문", value='너에게 묻는다 \n 연탄재 함부로 발로 차지 마라 \n 너는 누구에게 한번이라도 뜨거운 사람이었느냐 \n 반쯤 깨진 연탄 \n 언젠가는 나도 활활 타오르고 싶을 것이다 \n 나를 끝 닿는데 까지 한번 밀어붙여 보고 싶은 것이다 \n 타고 왔던 트럭에 실려 다시 돌아가면 \n 연탄, 처음으로 붙여진 나의 이름도 \n 으깨어져 나의 존재도 까마득히 뭉개질 터이니 \n 죽어도 여기서 찬란한 끝장을 한번 보고 싶은 것이다 \n 나를 기다리고 있는 뜨거운 밑불위에 \n 지금은 인정머리없는 차가운, 갈라진 내 몸을 얹고 \n 아랫쪽부터 불이 건너와 옮겨 붙기를 \n 시간의 바통을 내가 넘겨 받는 순간이 오기를 \n 그리하여 서서히 온몸이 벌겋게 달아 오르기를 \n 나도 느껴보고 싶은 것이다 \n 나도 보고 싶은 것이다 \n \n 모두들 잠든 깊은 밤에 눈에 빨갛게 불을 켜고 \n 구들장 속이 얼마나 침침하니 손을 뻗어 보고 싶은 것이다 \n 나로 하여 푸근한 잠 자는 처녀의 등허리를 \n 밤새도록 슬금슬금 만져도 보고 싶은 것이다', inline=False)
    embed.set_footer(text="시집 〈외롭고 높고 쓸쓸한〉 (1994) \npoem code: 8")
    await ctx.send(embed=embed)

@bot.command()
async def 테스트2(ctx):
    embed = discord.Embed(title="풀꽃", description="나태주", color=0x0048ba)
    embed.add_field(name="본문", value='자세히 보아야 사랑스럽다 \n 오래 보아야 사랑스럽다 \n 너도 그렇다', inline=False)
    embed.set_footer(text="시집 〈종려나무〉 (2009) \npoem code: 2")
    await ctx.send(embed=embed)

@bot.command()
async def 시(ctx):
    dm_channel = await ctx.message.author.create_dm()(ctx.author.id).send()
    await dm_channel.send(f"테스트 멘션이에요!")

@bot.command()
async def 예문(ctx):
    await ctx.send("{} 예문을 DM으로 보내드렸어요!".format(ctx.author.mention))


##영어판

@bot.command()
async def guidebook(ctx):
    embed = discord.Embed(title="guidebook", description="Foxbot guidebook", color=0x0048ba)
    embed.add_field(name="English guidebook is not supported yet... :smiling_face_with_tear: ", value='see you soon when I pdate', inline=False)
    embed.set_footer(text="let's learn Korean! 'fighting!'")
    await ctx.send(embed=embed)

bot.run(token)
app.run(token)
