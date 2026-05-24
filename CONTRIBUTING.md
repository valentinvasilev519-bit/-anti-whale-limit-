<!-- Contributing Guidelines -->

# 🤝 Contributing to This Project

Благодаря че искаш да допринесеш! Следи тези указания.

## 📋 Before You Start

1. **Fork** хранилището
2. **Clone** локално: `git clone https://github.com/твоеПотребителскоИме/проект.git`
3. **Create branch**: `git checkout -b feature/твоята-функция`

## 🚀 Development Workflow

### 1. Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Копирай .env файл
cp .env.example .env
```

### 2. Make Changes

- Следи кодирания стил на проекта
- Напиши descriptive commits
- Добавяй тестове за нов код
- Ъпдейтай документацията

### 3. Testing

```bash
pylint **/*.py
black --check .
pytest
```

### 4. Commit

```bash
git add .
git commit -m "type: description"
```

**Commit Types:**
- `feat:` - Нова функция
- `fix:` - Поправка на грешка
- `docs:` - Документация
- `style:` - Форматиране
- `refactor:` - Преструктуриране
- `test:` - Тестове
- `chore:` - Maintenance

### 5. Push & Pull Request

```bash
git push origin feature/твоята-функция
```

После отвори PR на GitHub с описание на промините.

## ✅ PR Checklist

- [ ] Кода е тестван
- [ ] Няма конфликти със main
- [ ] Документацията е обновена
- [ ] Commit messages са descriptive
- [ ] Няма hardcoded secrets/keys

## 🎯 Code Quality Standards

- **Lint:** ✅ Трябва да pass
- **Tests:** ✅ Всички tests трябва да pass
- **Coverage:** ≥ 80% (където е възможно)
- **Documentation:** ✅ Всички функции документирани

## 🔐 Security

- **Никога** не пушвай secrets
- **Никога** не commitvай `.env` файлове
- Докладвай уязвимостите приватно

## ❓ Questions?

- GitHub Issues за bugs
- Discussions за questions
- Email за security issues

---

**Thank you for contributing!** 🎉
