import asyncio
import discord

app = discord.Client()
token = ""

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
    embed.add_field(name="난이도?", value="난이도는 1부터 10까지 있어요. (kr <장르> 단계1, 단계2, 단계3...) 그리고 진짜 어려운 'X' 단계도 있어요! (kr <장르> 단계X) 한번 도전해보시겠어요? :fire: :rooster: :ramen:", inline=False)
    embed.add_field(name="kr 소설 (난이도)", value="레벨에 맞는 소설 지문 일부를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
    embed.add_field(name="kr 시 (난이도)", value="레벨에 맞는 시를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
    embed.add_field(name="kr 대사 (난이도)", value="레벨에 맞는 영화, 드라마 등의 대사를 무작위로 뽑아 DM으로 보내드려요.", inline=False)
    embed.add_field(name="kr (장르) 번호 (숫자)", value="지정한 글을 DM으로 보내드려요. DM으로 보내진 모든 글 하단에는 고유 번호가 있는데, 좋아하는 글을 다시 보고 싶으시다면 그 숫자를 기록해주셔도 좋아요!", inline=False)
    embed.add_field(name="kr 모든 (장르)", value="지정한 글 종류가 총 몇 개 수록되어있는 지 알려드려요!", inline=False)
    embed.add_field(name="kr 수필", value="폭스봇 주인이 자기 생각을 적은 노트가 있는데 그 중에서 아무거나 한 장을 뜯어서 뽑아 DM으로 보내드려요! ㅋㅋㅋㅋㅋㅋ", inline=False)
    embed.set_footer(text="다들 한국어 열심히 배워봐요! 화이팅!")
    await ctx.send(embed=embed)

@bot.command(aliases=['시 단계1'])
async def 시1(ctx):
    embed = discord.Embed(title="풀꽃", description="나태주", color=0x0048ba)
    embed.add_field(name="본문", value='자세히 보아야 사랑스럽다 \n 오래 보아야 사랑스럽다 \n 너도 그렇다', inline=False)
    embed.set_footer(text="시집 〈종려나무〉 (2009) \npoem code: 2\n level 2")
    await ctx.send(embed=embed)

@bot.command(aliases=['시 단계2'])
async def 시2(ctx):
    embed = discord.Embed(title="풀꽃", description="나태주", color=0x0048ba)
    embed.add_field(name="본문", value='자세히 보아야 사랑스럽다 \n 오래 보아야 사랑스럽다 \n 너도 그렇다', inline=False)
    embed.set_footer(text="시집 〈종려나무〉 (2009) \npoem code: 2")
    await ctx.send(embed=embed)

@bot.command(name = "테스트")
async def 단계1(ctx, 단계1):
    embed = discord.Embed(title="풀꽃", description="나태주", color=0x0048ba)
    embed.add_field(name="본문", value='자세히 보아야 사랑스럽다 \n 오래 보아야 사랑스럽다 \n 너도 그렇다', inline=False)
    embed.set_footer(text="시집 〈종려나무〉 (2009) \npoem code: 2")
    await ctx.send(embed=embed)

async def 단계2(ctx, 단계2):
    embed = discord.Embed(title="백범 일지", description="김구", color=0x0048ba)
    embed.add_field(name="나의 소원", value='"네 소원이 무엇이냐?" 하고 하느님이 물으시면, 나는 서슴지 않고\n "내 소원은 대한 독립이오"하고 대답할 것이다. \n\n "그 다음 소원은 무엇이냐?" 하면, 나는 또 \n "우리나라의 독립이오" 할 것이요, 또, \n\n "그 다음 소원이 무엇이냐?" 하는 세 번째 물음에도, 나는 더욱 소리를 높여서, \n "나의 소원은 우리나라 대한의 완전한 자주독립이오."하고 대답할 것이다. \n\n 동포 여러분! \n 나 김구의 소원은 이것 하나밖에는 없다. 내 과거의 70 평생을 이 소원을 위해 살아왔고, 현재에도 이 소원 때문에 살고 있고, 미래에도 나는 이 소원을 달(達)하려고 살 것이다.', inline=False)
    embed.set_footer(text="수필 〈백범 일지〉 (1929) \nessay code: 1\nlevel 4")
    await ctx.send(embed=embed)


@bot.command()
async def 시(ctx):
    dm_channel = await ctx.message.author.create_dm()(ctx.author.id).send()
    await dm_channel.send(f"테스트 멘션이에요!")

@bot.command()
async def 예문(ctx):
    await ctx.send("{} 예문을 DM으로 보내드렸어요!".format(ctx.author.mention))
    await member.send(f'테스트 성공')
    await message.author.send("Content")
    await client.get_user(other_user_id).send("Content")

@bot.command(name="DM보내기", pass_context=True)
async def send_dm(ctx, user_name: discord.member):
    channel = await user_name.create_dm()
    await channel.send("예제 성공했어요!")


##영어판

@bot.command()
async def guidebook(ctx):
    embed = discord.Embed(title="guidebook", description="Foxbot guidebook", color=0x0048ba)
    embed.add_field(name="English guidebook is not supported yet... :smiling_face_with_tear: ", value='see you soon when I update', inline=False)
    embed.set_footer(text="let's learn Korean! 'fighting!'")
    await ctx.send(embed=embed)


## 이스터에그

@bot.command()
async def 보티랑대화해봐(ctx):
    await ctx.channel.send('!보티 뭐하냐')

@bot.command(aliases=['what?'])
async def boti2(ctx):
    await ctx.channel.send('왜 그래 쌀쌀맞게')

bot.run(token)
app.run(token)
