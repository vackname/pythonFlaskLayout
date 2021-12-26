import config
import controllers.Home

#域名
host='127.0.0.1'
#port 號
port=3131
if __name__ == '__main__':
    # 啟動flask
    config.app.run(host=host, port=port)
