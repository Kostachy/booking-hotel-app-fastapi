import pytest
from httpx import AsyncClient


@pytest.mark.parametrize('email,password,status_code', [
    ('kot@pes.com', 'kotopes', 200),
    ('kot@pes.com', 'kot0pes', 409),
    ('abc@pes.com', 'pesokot', 200),
    ('abcxxxom', 'pesoxxxot', 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/register', json={
        'email': email,
        'password': password
    })
    assert response.status_code == status_code


@pytest.mark.parametrize('email,password,status_code', [
    ('test@test.com', 'test', 200),
    ('krut@example.com', 'test', 200)
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post('/auth/login', json={
        'email': email,
        'password': password
    })
    assert response.status_code == status_code
