import pynecone as pc

def get_input_field(icon: str, placeholder: str, _type: str):
    return pc.container(
        pc.hstack(
            pc.icon(
                tag=icon,
                color='black',
                fontSize='12px',
            ),
            pc.input(
                placeholder=placeholder,
                border='0px',
                focus_border_color='black',
                fontWeight='semibold',
                fontSize='13px',
                type=_type,
            ),
        ),
        borderBottom='0.3px solid green',
        width='300px',
        height='43px',
    )


def index():
    login_container = pc.container(
        pc.vstack(
            pc.container(height= '75px'),
            pc.container(
                pc.text(
                    'ONESTARGRAM',
                    style= {
                        "fontSize": "25px",
                        "fontWeight": "bolder",
                        "letterSpacing": "5px",
                        "fontFamily": "Georgia, Serif",
                        "background": "-webkit-linear-gradient(-45deg, #fa0000, #f0b46c)",
                        "-webkit-background-clip": "text",
                        "color": "transparent",
                    },
                    center_content =True,
                ),
            ),
        ),
        pc.vstack(
            pc.container(height= '10px'),
            pc.container(
                pc.image(
                    src="favicon.ico",  # 이미지 파일의 경로를 지정합니다.
                    alt="ONE STAR",  # 이미지의 대체 텍스트를 지정합니다.
                    style={"width": "100px", "height": "100px"},  # 이미지 크기를 조정합니다.
                ),
                style={
                    "width": "100%",  # 부모 컨테이너의 100% 너비 설정
                    "display": "flex",
                    "flex-direction": "column",  # 내부 컨테이너의 내용을 세로로 정렬
                    "align-items": "center",  # 내부 컨테이너의 내용을 수직으로 가운데 정렬
                    },
                ),
            pc.container(height='120px'),
            get_input_field('Email','Email',''),
            get_input_field('Lock','Password','password'),
            pc.button(
                pc.text(
                    '비밀번호를 잊어버리셨나요?',
                    style = {
                        'fontSize':'12px',
                        'color':'black',
                        'textAlign':'end',
                    },
                ),
                style = {
                    'float':'right',
                },
            ),
            pc.container(height='55px'),
            pc.hstack(
                pc.button(
                    pc.text(
                        '회원가입',
                        style = {
                            'color':'white',
                            'fontSize':'13px',
                            'weight':'bolder',
                        },
                    ),
                    color_scheme='blue',
                ),
                pc.container(width='130px'),
                pc.button(
                    pc.text(
                        '로그인',
                        style={
                            'color':'white',
                            'fontSize':'13px',
                            'weight':'bolder',
                            'textAlign':'end',
                        },
                    ),
                    color_scheme='blue',
                )
            ),
        ),
        
        width ='500px',
        height='75vh',
        center_content=True,
        bg = '#ffffff',
        borderRadius='15px',
        boxShadow='-11px 11px 50px #9ecadb'
    )

    _main = pc.container(
        login_container,
        center_content=True,
        justifyContent='center',
        maxWidth='auto',
        #width='80vh' 가로 길이
        height='100vh', #세로 길이
        bg='#000000', #배경 색상
    )
    return _main


app = pc.App()
app.add_page(index)
app.compile()