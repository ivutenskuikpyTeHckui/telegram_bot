from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Hr(StatesGroup):
    check_man = State()
    choose_man = State()
    psychotype_man_and_women = State()
    expert_video = State()
    important_skill_before_relationships = State()
    invitation_competition = State()
    what_is_important_things_for_relationships = State()
    important_things_for_relationships = State()
    course = State()
    first_lesson = State()
    payment = State()
    not_pay_after_2_days = State()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Hr.check_man)
    await message.answer("Чтобы посмотреть мужчин нажмите кнопку 'Посмотреть'",
                         reply_markup=kb.check_man)
    
@router.message(Hr.check_man)
async def pictures_with_describe(message:Message, state: FSMContext):
    await state.update_data(check_man=message.text)
    await state.set_state(Hr.choose_man)
    await message.answer(text="Выбери мужчину, с которым ты готова пойти на свидание", reply_markup=kb.choose_man)
    media_photo = [
        InputMediaPhoto(media='AgACAgIAAxkBAAMRZw7snnh4ht4WVXI5L1TZojnlKzcAAhLpMRsuGXlIf8k2JgwvvesBAAMCAAN4AAM2BA', 
        caption="Описание 1 мужчины"),
        InputMediaPhoto(media='AgACAgIAAxkBAAMRZw7snnh4ht4WVXI5L1TZojnlKzcAAhLpMRsuGXlIf8k2JgwvvesBAAMCAAN4AAM2BA', 
        caption="Описание 2 мужчины"),
        InputMediaPhoto(media='AgACAgIAAxkBAAMRZw7snnh4ht4WVXI5L1TZojnlKzcAAhLpMRsuGXlIf8k2JgwvvesBAAMCAAN4AAM2BA', 
        caption="Описание 3 мужчины"),
        InputMediaPhoto(media='AgACAgIAAxkBAAMRZw7snnh4ht4WVXI5L1TZojnlKzcAAhLpMRsuGXlIf8k2JgwvvesBAAMCAAN4AAM2BA', 
        caption="Описание 4 мужчины"),
    ]
    await message.answer_media_group(media=media_photo)
    

@router.message(Hr.choose_man)
async def get_psychotype_man_and_women(message:Message, state:FSMContext):
    await state.update_data(choose_man=message.text)
    await state.set_state(Hr.psychotype_man_and_women)
    match message.text:
        case "1":
            await message.answer("Психотип мужчины: 'Описание психотипа'.\n Ваш психотип: 'Описание психотипа'.", 
                                 reply_markup=kb.expert_video)
        case "2":
            await message.answer("Психотип мужчины: 'Описание психотипа'.\n Ваш психотип: 'Описание психотипа'.",
                                 reply_markup=kb.expert_video)
        case "3":
            await message.answer("Психотип мужчины: 'Описание психотипа'.\n Ваш психотип: 'Описание психотипа'.",
                                 reply_markup=kb.expert_video)
        case "4":
            await message.answer("Психотип мужчины: 'Описание психотипа'.\n Ваш психотип: 'Описание психотипа'.",
                                 reply_markup=kb.expert_video)

@router.message(Hr.psychotype_man_and_women)
async def expert_video(message:Message, state: FSMContext):
    await state.update_data(psychotype_man_and_women = message.text)
    await state.set_state(Hr.expert_video)
    await message.answer("'здесь будет видео'", 
                         reply_markup=kb.important_skill_before_relationships)
    
@router.message(Hr.expert_video)
async def invitation_competition(message:Message, state:FSMContext):
    await state.update_data(expert_video=message.text)
    await state.set_state(Hr.important_skill_before_relationships)
    await message.answer(text="Важный навык перед построением отношений - это умение проводить время с собой",
                         reply_markup=kb.invitation_competition)
    await message.answer_photo(photo='AgACAgIAAxkBAAMRZw7snnh4ht4WVXI5L1TZojnlKzcAAhLpMRsuGXlIf8k2JgwvvesBAAMCAAN4AAM2BA')

@router.message(Hr.important_skill_before_relationships)
async def invitation_competition(message: Message, state: FSMContext):
    await state.update_data(important_skill_before_relationships=message.text)
    await state.set_state(Hr.invitation_competition)
    await message.answer(
        "Я приглашаю тебя принять участие в конкурсе, где ты можешь выиграть свидание с собой в ресторане или спа. Я подберу для тебя достойное место в твоем городе место, которое будет приятным сюрпризом. переходи по ссылке чтобы учавствовать.\n https://chatgpt.com/c/6710ccf3-5498-800c-afb7-975be46be78b",
                         reply_markup=kb.what_is_important_things_for_relationships)
    
@router.message(Hr.invitation_competition)
async def what_is_important_things_for_relationships(message:Message, state:FSMContext):
    await state.update_data(invitation_competition=message.text)
    await state.set_state(Hr.what_is_important_things_for_relationships)
    await message.answer("Как думаешь что самое важное для построения отношений?", 
                         reply_markup=kb.things_for_relationship)

@router.message(Hr.what_is_important_things_for_relationships)
async def important_things_for_relationships(message:Message, state:FSMContext):
    await state.update_data(what_is_important_things_for_relationships=message.text)
    await state.set_state(Hr.important_things_for_relationships)
    match message.text:
        case "Самоценность": 
            await message.answer(f"Ты права, {message.text.lower()} это то, от чего зависят здоровые отношения, а так же важно развивать  женственность и коммуникацию и учится разговаривать с мужчиной на одном языке.", 
                                 reply_markup=kb.course)
        case "Женственность": 
            await message.answer(f"Ты права, {message.text.lower()} это то, от чего зависят здоровые отношения, а так же важно развивать самоценность и коммуникацию и учится разговаривать с мужчиной на одном языке.", 
                                 reply_markup=kb.course)
        case "Коммуникация": 
            await message.answer(f"Ты права, {message.text.lower()} это то, от чего зависят здоровые отношения, а так же важно развивать самоценность и женственность и учится разговаривать с мужчиной на одном языке.", 
                                 reply_markup=kb.course)

@router.message(Hr.important_things_for_relationships)
async def course(message:Message, state:FSMContext):
    await state.update_data(important_things_for_relationships=message.text)
    await state.set_state(Hr.course)
    await message.answer(text= '''
                         Как научится всему этому я заложила в свой курс «любовь к себе гарантия любви мужчины»\n 'ссылка на описание курса'.
                         ''' , 
                         reply_markup=kb.first_lesson)
    
@router.message(Hr.course)
async def first_lesson(message:Message, state:FSMContext):
    await state.update_data(course=message.text)
    await state.set_state(Hr.first_lesson)


    await message.answer(text='''
    Для бесплатного первого урока подпишись на канал 'ссылка на канал'.
    ''',
    )

    '''
    здесь будет реализация проверки на подкписку на канал,по дефолту будет выдавать, что пользователь подписан 
    после проверки будет выдаваться ссылка на видеоурок
    ''' 
    await message.answer(text="'Ссылка на видеоурок'", reply_markup=kb.payment)

@router.message(Hr.first_lesson)
async def payment(message:Message, state:FSMContext):
    await state.update_data(first_lesson=message.text)
    await state.set_state(Hr.payment)
    await message.answer(text='''
                         Если ты готова присоединиться переходи по ссылке для оплаты и я добавлю тебя в группу курса, где ты получишь все важные материалы для построения счастливых отношений.\n 'ссылка на оплату курса'.
                         ''',
                         
                         )



