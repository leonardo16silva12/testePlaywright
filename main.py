from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  # headless -> modo segundo plano
    page = navegador.new_page()
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("http://192.168.0.53:8080/troppus/vue/tab/tab658/form.do")
    page.keyboard.press('F11')

    # LOGIN
    t1 = page.locator("input[name=id]")
    t1.fill("MASTER")
    time.sleep(2)

    t2 = page.locator("input[name=senha]")
    t2.fill("MSTR")
    time.sleep(2)

    t3 = page.locator("input[value=Login]").click()
    time.sleep(5)

    t4 = page.locator("//tbody/tr[1]/td[1]/button[1]").click()
    time.sleep(2)

    t5 = page.locator("//img[@title='Supervisor']").click()
    time.sleep(2)

    # CREATE
    t6 = page.locator("//input[@name='form.codigoBanco']")
    t6.fill("999")
    time.sleep(2)
    page.keyboard.press('Tab')
    time.sleep(2)

    t7 = page.locator("//input[@name='form.codigoRemessa']")
    t7.fill("77")
    time.sleep(2)
    page.keyboard.press('Tab')
    time.sleep(2)

    t8 = page.locator("//input[@name='form.remessaDescricao']")
    t8.fill("TST")
    time.sleep(4)
    page.keyboard.press('Tab')
    time.sleep(2)

    t9 = page.locator("//button[@title='Salvar']").click()
    time.sleep(2)

    # READ
    t6.fill("999")
    page.keyboard.press('Tab')
    time.sleep(2)
    t7.fill("77")
    page.keyboard.press('Tab')
    time.sleep(2)

    # UPDATE
    t8.fill("TST ALTERACAO")
    time.sleep(4)

    t10 = page.locator("//button[@title='Salvar']").click()
    time.sleep(2)

    # DELETE
    t6.fill("999")
    page.keyboard.press('Tab')
    time.sleep(2)
    t7.fill("77")
    page.keyboard.press('Tab')
    time.sleep(2)

    t11 = page.locator("//button[@title='Excluir']").click()
    time.sleep(2)

    t12 = page.locator("//span[normalize-space()='Confirmar']").click()
    time.sleep(2)

    # LOGOUT
    t13 = page.locator("//img[@src='/troppus/images/user_icon.png']").click()
    time.sleep(2)

    t14 = page.locator("//a[@id='btn-logout']").click()
    time.sleep(5)

    page.close()
